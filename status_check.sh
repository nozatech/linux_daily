#!/bin/bash
# Check and put ok status if the RRS game service is running for Lobby 7504 & 7505 services

if (( $(ps aux | grep ./RRServer_0328_7504 | wc -l) > 0  &&  $(ps aux | grep ./RRServer_0328_7505 | wc -l) > 0 )); then
        echo OK > /var/www/html/status/index.html;
else rm /var/www/html/status/index.html > /dev/null 2>&1;
fi

