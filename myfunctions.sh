Create a function file called myfunctions.sh:



#!/bin/bash
# set variables
declare -r TRUE=0
declare -r FALSE=1
declare -r PASSWD_FILE=/etc/passwd
##################################################################
# Purpose: Converts a string to lower case
# Arguments:
# $1 -> String to convert to lower case
##################################################################
function to_lower()
{
local str="$@"
local output
output=$(tr '[A-Z]' '[a-z]'<< Message
# $2 -> Exit status (optional)
##################################################################
function die()
{
local m="$1"	# message
local e=${2-1}	# default exit status 1
echo "$m"
exit $e
}
##################################################################
# Purpose: Return true if script is executed by the root user
# Arguments: none
# Return: True or False
##################################################################
function is_root()
{
[ $(id -u) -eq 0 ] && return $TRUE || return $FALSE
}
##################################################################
# Purpose: Return true $user exits in /etc/passwd
# Arguments: $1 (username) -> Username to check in /etc/passwd
# Return: True or False
##################################################################
function is_user_exits()
{
local u="$1"
grep -q "^${u}" $PASSWD_FILE && return $TRUE || return $FALSE
}

You can load myfunctions.sh into the current shell environment, enter:
$ .myfunctions.sh
OR
$ ./path/to/myfunctions.sh