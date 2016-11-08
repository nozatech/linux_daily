FizzBuzz in Bash


############
# for loop #
############

#!/bin/bash
## All arithmetic has to use ((    )) 

for i in {1..30}; do
        if (( $i % 3 == 0 )) && (( $i % 5 == 0 )); then echo "for-loop"
                elif (( $i % 3 == 0 )); then echo "for"
                elif (( $i % 5 == 0 )); then echo "loop"
        else echo $i;
        fi
done


#!/bin/bash
## C style
for ((i=0; i<=30; i++)); do
    if (( $i % 3 == 0 )) && (( $i % 5 == 0 )); then echo "for-loop"
    elif (( $i % 3 == 0 )); then echo "for"
    elif (( $i % 5 == 0 )); then echo "loop"
    else echo $i;
    fi
done


#
echo
sleep 2
#

################
# while loop-1 #
################

#!/bin/bash
i=1
while (( i < 31 ));
do
        if (( $i % 3 == 0 )) && (( $i % 5 == 0 )); then echo "While-Loop"
        elif (( $i % 3 == 0 )); then echo "While"
        elif (( $i % 5 == 0 )); then echo "Loop"
        else echo "$i";
        fi
((i++))
done

#
echo
sleep 2
#


################
# while loop-2 #
################

i=1;
while (( i < 31 ));
do
        if { ( (( i % 5 == 0 )) && (( i % 3 == 0 )) ) } then echo "while-loop";
        elif (( i % 3 == 0 )); then echo "while";
        elif (( i % 5 == 0 )); then echo "loop";
        else
                echo "$i";
        fi
(( i++ ))
done



###
echo
sleep 2
###

################
# while loop-3 #
################

i=1
while [ $i -ne 31 ]
do
    if { ( (( i % 5 == 0 )) && (( i % 3 == 0 )) ) } then echo "while - loop";
    elif (( i % 3 == 0 )); then echo "while";
    elif (( i % 5 == 0 )); then echo "loop";
    else
        echo "$i";
    fi

    i=$(( $myvar + 1 ))
done


################
# Until loop-3 #
################

i=1
until [ $i -eq 31 ]
do
    if { ( (( i % 5 == 0 )) && (( i % 3 == 0 )) ) } then echo "Util - Loop";
    elif (( i % 3 == 0 )); then echo "Until";
    elif (( i % 5 == 0 )); then echo "Loop";
    else
        echo "$i";
    fi

    i=$(( $i + 1 ))
done


##################
### Python ###
##################

### While Loop

#!/usr/bin/python3
count = 0
while count < 101:
    if count % 5 == 0 and count % 3 == 0:
        print "FizzBuzz"
    elif count % 3 == 0:
        print "Fizz"
    elif count % 5 == 0:
        print "Buzz"
    else:
        print count

    count = count + 1    # this will get executed every loop
	
### for loop

for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        print "FizzBuzz"
    elif num % 3 == 0:
        print "Fizz"
    elif num % 5 == 0:
        print "Buzz"
    else:
        print num
		

for num in xrange(1,101):
    if num % 5 == 0 and num % 3 == 0:
        msg = "FizzBuzz"
    elif num % 3 == 0:
        msg = "Fizz"
    elif num % 5 == 0:
        msg = "Buzz"
    else:
        msg = str(num)
    print msg

for num in xrange(1,101):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:       # no more elif
        msg += 'Buzz'
    if not msg:      # check if msg is an empty string
        msg += str(num)
    print msg

#!/usr/bin/python
for num in xrange(1,101):
    msg = ''
    if num % 3 == 0:
        msg += 'Fizz'
    if num % 5 == 0:
        msg += 'Buzz'
    print msg or num
$python fz.py




