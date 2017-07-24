#!/bin/bash
# RRS Check and put ok status if the RRS game service is running for Lobby 7504 & 7505 services
# Add to crontab -e "5 * * * * /root/bin/status.sh > /dev/null 2>&1 "

if (( $(ps aux | grep ./RRServer_0328_7504 | grep -v grep | wc -l) > 0  &&  $(ps aux | grep ./RRServer_0328_7505  grep -v grep || wc -l) > 0 )); then
        echo OK > /var/www/html/status/index.html;
else rm -f /var/www/html/status/index.html > /dev/null 2>&1;
fi


#!/bin/bash
# PMF Httpd process check and put ok status
# Add to crontab -e "5 * * * * /root/bin/status.sh > /dev/null 2>&1 "

if (( $(ps aux | grep httpd | grep -v grep | wc -l) > 0  &&  $(ps aux | grep httpd| grep -v grep |wc -l) > 0 )); then
        echo ok > /var/www/html/status/index.html;
else rm -f /var/www/html/status/index.html > /dev/null 2>&1;
fi





#!/bin/bash

### lobby 7505 ###

RRSERVER="RRServer_7505"

ps aux | grep -v grep | grep ./RRServer_0617_7505 > /dev/null 2>&1

if [ $? != 0 ]
   then
		
		/$RRSERVER/start-us-lobby-7505.sh
fi

##################
### lobby 7504 ###
##################

RRSERVER="RRServer_7504"

ps aux | grep -v grep | grep ./RRServer_0402_7504 >/dev/null 2>&1

if [ $? != 0 ]
   then
		/$RRSERVER/start-us-lobby-7504.sh
fi




./RRServer_0417_7505 slave port 7510 mAddress 10.130.33.41 mPort 7505 publicAddress 128.199.203.10 maxConnections 500
 start-us-s1.sh