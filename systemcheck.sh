#! /bin/bash

### Result should be same as below ###-------------------------
#Internet:  Connected
#Operating System Type :  GNU/Linux
#OS Name : CentOS Linux
#cpe:/o:centos:centos:7
#OS Version : 7 (Core)
#7
#7
#Architecture :  x86_64
#Kernel Release :  3.10.0-327.36.3.el7.x86_64
#Hostname :  i7
#Internal IP :  10.100.5.155
#External IP :  65.87.26.125
#Name Servers :  namco.local 10.10.1.10
#Logged In users :
#apark    pts/0        2016-12-06 09:12 (10.100.5.190)
#Ram Usages :
#              total        used        free      shared  buff/cache   available
#Mem:           7.6G        140M        7.3G        8.5M        147M        7.3G
#Swap Usages :
#              total        used        free      shared  buff/cache   available
#Swap:          7.7G          0B        7.7G
#Disk Usages :
#Filesystem               Size  Used Avail Use% Mounted on
#/dev/sda1                497M  167M  331M  34% /boot
#Load Average :  average:0.05,0.03,
#System Uptime Days/(HH:MM) :  46 min
#----------------------------------------------------------------------------------



# unset any variable which system may be using
# clear the screen
clear

unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

while getopts iv name
do
        case $name in
          i)iopt=1;;
          v)vopt=1;;
          *)echo "Invalid arg";;
        esac
done

#----------------------------------------------------------------------------------
if [[ ! -z $iopt ]]; then
{
wd=$(pwd)
basename "$(test -L "$0" && readlink "$0" || echo "$0")" > /tmp/scriptname
scriptname=$(echo -e -n $wd/ && cat /tmp/scriptname)
su -c "cp $scriptname /usr/bin/monitor" root && echo "Script has Installed, run 'monitor' Command" || echo "Installation failed"
}
fi
#----------------------------------------------------------------------------------
if [[ ! -z $vopt ]]; then
{
echo -e "tecmint_monitor version 0.1\nDesigned by Tecmint.com\nReleased Under Apache 2.0 License"
}
fi
#----------------------------------------------------------------------------------
if [[ $# -eq 0 ]] ; then
{
# Define Variable tecreset
tecreset=$(tput sgr0)

# Check if connected to Internet or not
ping -c 1 google.com &> /dev/null && echo -e '\E[32m'"Internet: $tecreset Connected" || echo -e '\E[32m'"Internet: $tecreset Disconnected"

# Check OS Type
os=$(uname -o)
echo -e '\E[32m'"Operating System Type :" $tecreset $os

# Check OS Release Version and Name
cat /etc/os-release | grep 'NAME\|VERSION' | grep -v 'VERSION_ID' | grep -v 'PRETTY_NAME' > /tmp/osrelease
echo -n -e '\E[32m'"OS Name :" $tecreset  && cat /tmp/osrelease | grep -v "VERSION" | cut -f2 -d\"
echo -n -e '\E[32m'"OS Version :" $tecreset && cat /tmp/osrelease | grep -v "NAME" | cut -f2 -d\"

# Check Architecture
architecture=$(uname -m)
echo -e '\E[32m'"Architecture :" $tecreset $architecture

# Check Kernel Release
kernelrelease=$(uname -r)
echo -e '\E[32m'"Kernel Release :" $tecreset $kernelrelease

# Check hostname
echo -e '\E[32m'"Hostname :" $tecreset $HOSTNAME

# Check Internal IP
internalip=$(hostname -I)
echo -e '\E[32m'"Internal IP :" $tecreset $internalip

# Check External IP
externalip=$(curl -s ipecho.net/plain;echo)
echo -e '\E[32m'"External IP : $tecreset "$externalip

# Check DNS
nameservers=$(cat /etc/resolv.conf | sed '1 d' | awk '{print $2}')
echo -e '\E[32m'"Name Servers :" $tecreset $nameservers

# Check Logged In Users
who>/tmp/who
echo -e '\E[32m'"Logged In users :" $tecreset && cat /tmp/who

# Check RAM and SWAP Usages
free -h | grep -v + > /tmp/ramcache
echo -e '\E[32m'"Ram Usages :" $tecreset
cat /tmp/ramcache | grep -v "Swap"
echo -e '\E[32m'"Swap Usages :" $tecreset
cat /tmp/ramcache | grep -v "Mem"

# Check Disk Usages
df -h| grep 'Filesystem\|/dev/sda*' > /tmp/diskusage
echo -e '\E[32m'"Disk Usages :" $tecreset
cat /tmp/diskusage

# Check Load Average
loadaverage=$(top -n 1 -b | grep "load average:" | awk '{print $10 $11 $12}')
echo -e '\E[32m'"Load Average :" $tecreset $loadaverage

# Check System Uptime
tecuptime=$(uptime | awk '{print $3,$4}' | cut -f1 -d,)
echo -e '\E[32m'"System Uptime Days/(HH:MM) :" $tecreset $tecuptime

# Unset Variables
unset tecreset os architecture kernelrelease internalip externalip nameserver loadaverage

# Remove Temporary Files
rm /tmp/osrelease /tmp/who /tmp/ramcache /tmp/diskusage
}
fi

shift $(($OPTIND -1))
                                                                                                                                                                            117,19        Bot
