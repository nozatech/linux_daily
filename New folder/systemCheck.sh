#!/bin/bash
# Purpose: Display various options to operator using menus
# Capture CTRL+C, CTRL+Z and QUIT singles using the trap
#--------------------------------------------------------
set -e

trap '' SIGINT   #2  same as CTRL+C
trap '' SIGQUIT  #3  same as q
trap '' SIGTSTP  #20 same as CTRL+Z

# display message, read input, and pause
pause() {                               # pause() function
    local mesg="$@"                     # make a local variable
    echo "$mesg"
    read -p "Press [Enter] key to continue..." key      # -p prompt output
}

# set an
while true   # same as 'while :'
do
    # show menu
    clear
    echo "---------------------------------"
    echo "       M A I N - M E N U"
    echo "---------------------------------"
    echo "1. Disk usage "
    echo "2. Biggest files usage "
    echo "3. Show what users are doing"
    echo "4. Show top memory process"
    echo "5. Show top CPU process"
    echo "6. Show network stats"
    echo "Type 'q' to Exit"
    echo "---------------------------------"
    read -r -p "Enter your choice [1-6] : " choice

    ### take actions using Case statement ###
    case $choice in

        1) pause "$(df -h | xargs | awk '{ print $11 " / " $9 " are free" }')";;

        #2) pause "$(sudo find / -type f -exec du -sh {} \; | sort -rh | head -n 5 2> /dev/null)";;

        2) pause "$(sudo find / -xdev -type f -size +100M -exec du -sh {} ';' | sort -rh | head -n10)";;

        3) pause "$(w | less)";;

        4) echo -e "\e[1;31m Top 10 Memory eating process: \e[0m"; ps -auxf | sort -nr -k 4 | head -10;
           echo; pause;;

        5) echo -e "\e[1;31m Top 10 CPU eating process:    \e[0m"; ps -auxf | sort -nr -k 3 | head -10;
           echo;  pause;;

        6) netstat -s | less;;

        q) break;;
        *) Pause "Select between 1 to 6 only or 'q' to quit."
    esac
done
