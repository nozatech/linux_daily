#!/bin/bash

rm -f /etc/nginx/conf.d/pingdom_ip.conf

curl https://my.pingdom.com/probes/ipv4 > /tmp/pingdom_ip.tmp

ips=`cat /tmp/pingdom_ip.tmp`

for ip in $ips

    do

        echo allow $ip; >> /etc/nginx/conf.d/pingdom_ip.conf
done
