#!/bin/bash
# NR collector 239 nslookup resolve issue
# to restart the nr service

tail -n 30 /var/log/newrelic/nrsysmond.log | grep "Couldn't resolve host 'collector-239.newrelic.com'"  > /dev/null

if [ $? = 0 ]; then
    sudo /etc/init.d/newrelic-sysmond restart
fi



# $ crontab -l

# NR collector 239 nslookup resolve issue
# to restart the NR service
*/5 * * * * /home/apark/newrelic/nr_restart.sh  2>&1  >> /home/apark/newrelic/log 


# 5 mins count down from Shell
for i in {1..300}; do echo -ne $i '\r'; sleep 1; done; echo