#!/bin/bash
 
# MySQL user
USER=root
 
# MySQL user password
PASSWORD=
 
# Percona Backup Home
PERCONA_BACKUP_HOME=/usr/sbin/innobackupex
 
# Remember when this script was started
DATE=`date +%G-%m-%d-%H-%M-%S`
 
# MySQL backup directory
BACKUP_DIR=$PERCONA_BACKUP_HOME/backup/$DATE
 
# filename where log file will be stored
LOG_FILENAME=$PERCONA_BACKUP_HOME/logs/percona-backup-$DATE.log
# Redirect stdout and stderr to file
# Preserve old decriptors
exec 3>&1 4>&2
# Open STDOUT as $LOG_FILE file for read and write.
exec 1<>$LOG_FILENAME
# Redirect STDERR to STDOUT
exec 2>&1
 
echo -e "\n\nStarting Percona Percona XtraBackup"
# We will use --no-timestamp since we will be using a custom folder
innobackupex --user=$USER --password=$PASSWORD $BACKUP_DIR --no-timestamp
 
if [ "$?" -ne "0" ]
then
        echo -e "\n\nThere was an error in the backup process. Stopping"
        exit 1
fi
 
innobackupex --apply-log $BACKUP_DIR
 
if [ "$?" -ne "0" ]
then
        echo -e "\n\nThere was an error in the backup process. Stopping"
        exit 1
fi
 
# Check if innobackupex completed successfully
count=$(cat $LOG_FILENAME | grep "innobackupex: completed OK" | wc -l)
if [ "$count" -ne "2" ]
then
        echo -e "\n\nHmm. There was an error during innobackupex. Please check the logs for more details"
    exit 1
fi
 
echo -e "\n\nTaring backup"
TAR_FILENAME=$PERCONA_BACKUP_HOME/percona-mysql-backup-$DATE.tar.gz
tar cvfpz $TAR_FILENAME $BACKUP_DIR
 
if [ "$?" -ne "0" ]
then
        echo -e "\n\nThere was an error in the backup process. Stopping"
    exit 1
fi
 
# I am adding this to this folder db-cluster/mysql-backup/daily but you can change this as you see fit
echo -e "\n\nSending data to Amazon S3."
s3cmd put $TAR_FILENAME s3://<bucket name>/db-cluster/mysql-backup/daily/
 
if [ "$?" -ne "0" ]
then
        echo -e "\n\nFailed to upload data to Amazon S3"
    exit 1
fi
 
echo -e "\n\nDeleting tmp data on Disk"
rm -R $BACKUP_DIR
rm -R $TAR_FILENAME
 
echo "Done. Log written to $LOG_FILENAME" >&3