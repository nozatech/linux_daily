#!/bin/bash

# Test an IP address for validity:
# Usage:
#      valid_ip IP_ADDRESS
#      if [[ $? -eq 0 ]]; then echo good; else echo bad; fi
#   OR
#      if valid_ip IP_ADDRESS; then echo good; else echo bad; fi
#

curl https://my.pingdom.com/probes/ipv4 > pingdom_ip.tmp
ips=pingdom_ip.tmp

function valid_ip()
{
    local  ip=$1
    local  stat=1

    if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        OIFS=$IFS
        IFS='.'
        ip=($ip)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
        stat=$?
    fi
    return $stat
}


# If run directly, execute some tests.
if [[ "$(basename $0 .sh)" == 'valid_ip' ]]; then
    ips=`curl https://my.pingdom.com/probes/ipv4 > pingdom_ip.tmp`
        
    for ip in $ips
    do
        if valid_ip $ip; then stat='good'; else stat='bad'; fi
        printf "%-20s: %s\n" "$ip" "$stat"
    done
fi