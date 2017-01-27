#!/bin/bash
# Poor man's MySQL Master/Slave replication monitoring script

USERNAME=
PASSWORD=
MASTER_HOST=192.168.1.1
MASTER_PORT=3306

SLAVE_HOST=192.168.1.2
SLAVE_PORT=3306

MYSQL="mysql -u $USERNAME -p$PASSWORD "
MASTER="$MYSQL -h $MASTER_HOST -P $MASTER_PORT"
SLAVE="$MYSQL -h $SLAVE_HOST -P $SLAVE_PORT"

$MASTER -e 'SHOW MASTER STATUS\G' > mstatus
$SLAVE -e 'SHOW SLAVE STATUS\G' > sstatus

function extract_value {
    FILENAME=$1
    VAR=$2
    grep -w $VAR $FILENAME | awk '{print $2}'
}

Master_Binlog=$(extract_value mstatus File )
Master_Position=$(extract_value mstatus Position )

Master_Host=$(extract_value sstatus Master_Host)
Master_Port=$(extract_value sstatus Master_Port)
Master_Log_File=$(extract_value sstatus Master_Log_File)
Read_Master_Log_Pos=$(extract_value sstatus Read_Master_Log_Pos)
Slave_IO_Running=$(extract_value sstatus Slave_IO_Running)
Slave_SQL_Running=$(extract_value sstatus Slave_SQL_Running)

ERROR_COUNT=0
if [ "$Master_Host" != "$MASTER_HOST" ]
then
    ERRORS[$ERROR_COUNT]="the slave is not replicating from the host that it is supposed to"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

if [ "$Master_Port" != "$MASTER_PORT" ]
then
    ERRORS[$ERROR_COUNT]="the slave is not replicating from the host that it is supposed to"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

if [ "$Master_Binlog" != "$Master_Log_File" ]
then
    ERRORS[$ERROR_COUNT]="master binlog ($Master_Binlog) and Master_Log_File ($Master_Log_File) differ"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

POS_DIFFERENCE=$(echo ${Master_Position}-$Read_Master_Log_Pos | bc)

if [ $POS_DIFFERENCE -gt 1000 ]
then
    ERRORS[$ERROR_COUNT]="The slave is lagging behind of $POS_DIFFERENCE"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

if [ "$Slave_IO_Running" == "No" ]
then
    ERRORS[$ERROR_COUNT]="Replication is stopped"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

if [ "$Slave_SQL_Running" == "No" ]
then
    ERRORS[$ERROR_COUNT]="Replication (SQL) is stopped"
    ERROR_COUNT=$(($ERROR_COUNT+1))
fi

if [ $ERROR_COUNT -gt 0 ]
then
    EMAIL=myname@gmail.com
    SUBJECT="ERRORS in replication"
    BODY=''
    CNT=0
    while [ "$CNT" != "$ERROR_COUNT" ]
    do
        BODY="$BODY ${ERRORS[$CNT]}"
        CNT=$(($CNT+1))
    done
    echo $SUBJECT
    echo $BODY
    echo $BODY | mail -s "$SUBJECT" $EMAIL
else
    echo "Replication OK"
    printf "file: %s at %'d\n" $Master_Log_File  $Read_Master_Log_Pos
fi

