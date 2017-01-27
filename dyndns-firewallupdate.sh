#!/bin/bash
#
# filename: dyndns-firewallupdate.sh
# Version: 0.1.0
#
# Script used to update iptables rules for a given number of dynamic IP:s.
#
# To run the script from root crontab:
# */5 * * * * /usr/local/bin/dyndns-firewallupdate.sh hostname1.domain1.com,hostname2.domain2.ne                                                                                              t 2>&1 >> /tmp/dyndns-firewallupdate.log

HOSTS=$1
CHAIN="INPUT"
IPTABLES="/sbin/iptables"
DATE=`date "+%F %T"`

# Argument to parse
if [ "${#@}" -ne "1" ]; then
echo "Usage: $0 [hostname] (several hosts can be specified comma separated with out spaces)"
exit 1
fi

IFS=","                                                 #Internal Field Seperator
# Check if we have old rules that should be removed
OLDCOUNT=`ls /tmp/host-* | wc -l`
NEWCOUNT=`for i in $HOSTS ; do echo $HOSTS ; done | wc -l`

if [ $OLDCOUNT -gt $NEWCOUNT ] ; then
echo "$DATE Old rules need to be removed"
rm /tmp/host-*
UPDATEFW=1
fi

for HOST in $HOSTS ; do
HOSTFILE="/tmp/host-$HOST"

# lookup host name from dns tables
IP=`/usr/bin/dig +short $HOST | /usr/bin/tail -n 1`
if [ "${#IP}" = "0" ]; then
echo "$DATE Couldn't lookup hostname for $HOST, failed."
continue
fi

OLDIP=""
if [ -a $HOSTFILE ]; then
OLDIP=`cat $HOSTFILE`
else
OLDIP="0.0.0.0"
fi

# save off new ip.
if [ $IP != $OLDIP ] ; then
echo $IP > $HOSTFILE
UPDATEFW=1
echo "$DATE $HOST should be updated."
else
echo "$DATE Same IP for $HOST, aborting".
continue
fi
done
unset IFS

if [ ! $UPDATEFW ] ; then
echo "$DATE No records to update"
exit 0
fi

# Flush old rules, will cause a very short interruption.
if [ "${#OLDIP}" != "0" ]; then
echo "$DATE Removing old rule ($OLDIP)"
`$IPTABLES -F $CHAIN`
fi

# Opening ports

for IP in `cat /tmp/host-*` ; do
echo "$DATE Inserting new rule ($IP)"

`$IPTABLES -A $CHAIN -s $IP/32 -p tcp --dport 5235 --syn -j ACCEPT`
`$IPTABLES -A $CHAIN -s $IP/32 -p tcp --dport 2195 --syn -j ACCEPT`
`$IPTABLES -A $CHAIN -s $IP/32 -p tcp --dport 2196 --syn -j ACCEPT`
done

# You can add static IPs or similar below.
#echo "$DATE Inserting new rule (description)"
#`$IPTABLES -A $CHAIN -s /32 -p tcp --dport 22 --syn -j ACCEPT`
#`$IPTABLES -A $CHAIN -s /32 -p icmp -j ACCEPT`
