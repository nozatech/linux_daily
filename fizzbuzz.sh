FizzBuzz


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




### Function ###
# functions to group pieces of code in a more logical way or practice the divine art of recursion.


#!/bin/bash

# A function to print "Hello World"
hello()
    { 
	  echo "Hello World"
	}
	
# Call the function
hello;

###

#!/bin/bash

function quit {
    exit
}
function hello {
    echo Hello!
}
hello
quit
echo foo


# test.sh for $1, $2, $3
#!/bin/bash

echo "\$1 is now $1"
echo "\$2 is now $2"
echo "\$3 is now $3"

# ./test.sh 1 2 3



