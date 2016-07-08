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
