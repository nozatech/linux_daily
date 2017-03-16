#!/bin/bash
# Installing Nagios4 Server on CentOS7 64bit Minimal version
# CentOS7 missing system sw & update

dhclient

yum -y update

###
# Install dependencies
###
yum -y install net-tools net-snmp vim gd gd-devel gcc glibc glibc-common make wget openssl openssl-devel httpd php epel-release

ifconfig

###
# Httpd service start
###
systemcltl start httpd.service
systemcltl status httpd.service
#yum repolist	#new EPEL repolist 

sleep 5

# yum grouplist | less
yum -y groupinstall "System Management" "System Administration Tools" "Development Tools"




###
# Installing Nagios4 on CentOS7 64bit Minimal version
#if test yum -y install wget make gcc glibc glibc-common libssl-dev openssl
#then
#        echo "CentOS installing necessary sw for compile..."
#else
#        sudo apt-get -y install wget make gcc glibc glibc-common libssl-dev openssl
#        echo "Ubuntu installing necessary sw for compile...."
#fi
###

###
# Step-2 :Create Nagios and Apache user account and group 
# Before compiling Nagios Core we need to create “nagios” user and group. When “nagios” user and 
# group is created, add “Apache” user to this group – this needs to be done due to some file permissions 
# which enable us to do actions via Nagios web interface.
# 
# Create a new nagcmd group for allowing external commands to be submitted through the web interface. 
# Add both the nagios user and the apache user to the group.
###
useradd -m nagios 
passwd nagios 
groupadd nagcmd 				#
usermod -a -G nagcmd nagios 
usermod -a -G nagcmd apache

###
# check to see the file is exist or download latest
###
NAGIOS_NEW="http://prdownloads.sourceforge.net/sourceforge/nagios/nagios-4.0.8.tar.gz"
NAGIOS_VER="4.0.8"

PLUGIN_NEW="http://www.nagios-plugins.org/download/nagios-plugins-2.0.3.tar.gz"
PLUGIN_VER="2.0.3"

NRPE_NEW="http://sourceforge.net/projects/nagios/files/nrpe-2.x/nrpe-2.15/nrpe-2.15.tar.gz"
NRPE_VER="2.15"

NAGIOS_HOME="/usr/local/nagios"
download="/tmp/download"

###
# Download folder check 
###
if [ -d $download ]; then
        echo "Directory exist"
        sleep 5
else
        echo "Creating $download directory...."
        mkdir -p $download
        sleep 5
fi

###
# Nagios download and compare version
###
if [ -e $download/nagios-$NAGIOS_VER.tar.gz  ]; then
        echo "nagios-$NAGIOS_VER file exist"
        sleep 5
else
        echo "Downloading file..."
        sleep 5
        cd $download
        wget $NAGIOS_NEW

fi

###
# Plugin download and compare version
###
if [ -e $download/nagios-plugins-$PLUGIN_VER.tar.gz  ]; then
        echo "Nagios plugins-$PLUGIN_VER.tar.gz file exist"
        sleep 5
else
        echo "Downloading file..."
        sleep 5
        cd $download
        wget $PLUGIN_NEW

fi

###
# NRPE download and compare version
###
if [ -e $download/nrpe-$NRPE_VER.tar.gz  ]; then
        echo "NRPE file exist"
        sleep 5
else
        echo "Downloading file..."
        sleep 5
        cd $download
        wget $NRPE_NEW

fi
### Download done!###

###
# Extract to /tmp/download  and Compile to install
###
tar xzvf $download/nagios-$NAGIOS_VER.tar.gz -C $download
tar xzvf $download/nagios-plugins-$PLUGIN_VER.tar.gz -C $download
tar xzvf $download/nrpe-$NRPE_VER.tar.gz -C $download

###
# Compile to install
###

# Nagios
cd $download
cd nagios-$NAGIOS_VER

./configure --with-command-group=nagicmd  #not nagios
make all
make install
make install-init
make install-commandmode
make install-config
make install exfoliation
make install-webconf		#Nagios' web interface



###
# Plugins
###
cd $download/nagios-plugins-$PLUGIN_VER
./configure --with-namgios-user=nagios --with-nagios-group=nagcmd
make
make install

###
# Nagios config check
###
echo "Nagios Config Check"
sleep 2
/usr/local/nagios/bin/nagios -v /usr/local/nagios/etc/nagios/cfg
sleep 5
echo "If there is error, please stop and check again."
sleep 5

###
# Create Nagios Web Interface user
# Create a nagiosadmin account for logging into the Nagios web interface. 
# Remember the password you assign to this account. You’ll need it while logging in to nagios web interface
###
htpasswd -c -B /usr/local/nagios/etc/htpasswd.users nagiosadmin

###
# Add service to run on boot
###
chkconfig --add nagios
chkconfig --level 35 nagios
###
# start nagios service
###
systemctl start nagios.service #or 

###
# Set up NRPE
###

cd $download/nrpe-$NRPE_VER
./configure --with-nagios-user=nagios --with-nagios-group=nagios --prefix=/usr/local
make all
sudo make install

###
# Install EPEL repository and "Nagios-plugins-all"
### 
# rpm -ivh https://ftp.fau.de/epel/beta/7/x86_64/epel-release-7-0.2.noarch.rpm
yum install epel-relase -y
yum install nagios-plugins-all -y
rm -rf /usr/local/nagios/libexec
ln -s /usr/lib64/nagios/plugins/ /usr/local/nagios/libexec
chown -R nagios:nagcmd /usr/local/nagios/libexec/


###
# Start and add in start up for Apache & Nagios
###
systemctl start httpd
systemctl enable httpd

# start nagios service and make it to start automatically on every boot.
systemctl start nagios		#/etc/init.d/nagios start   #systemctl start nagios || systemctl start nagios.service
chkconfig --add nagios
chkconfig nagios on



###
# CentOS7 using firewalld to enable port 80
###
firewall-cmd --zone=public --add-port=http/tcp
firewall-cmd --zone=public --add-port=http/tcp --permanent
systemctl restart firewalld

###
# Adjust SELinux Settings
###
# By default, SELinux will be in enforcing mode, and it throws “Internal Server Error” 
# messages when you attempt to access the Nagios CGIs.
# To rectify this error, edit file /etc/selinux/config:
# vi /etc/selinux/config
# And, set SELinux to permissive mode.
#[...
#SELINUX=permissive


###
# Config Nagios
###
# admin email info
#vi /usr/local/nagios/etc/objects/contacts.cfg
#
# Uncomment and Change lines as shown below 
#Order deny,allow
#Deny from all
#Allow from 127.0.0.1 192.168.1.0/24
