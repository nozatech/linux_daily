#!/bin/bash
# NR collector 239 nslookup resolve issue
# to restart the nr service

tail -n 30 /var/log/newrelic/nrsysmond.log | grep "Couldn't resolve host 'collector-239.newrelic.com'"  > /dev/null

if [ $? = 0 ]; then
    sudo /etc/init.d/newrelic-sysmond restart
fi
