FizzBuzz


############
# for loop #
############

#!/bin/bash

for i in {1..30}; do
        if (( $i % 3 == 0 )) && (( $i % 5 == 0 )); then echo "for-loop"
                elif (( $i % 3 == 0 )); then echo "for"
                elif (( $i % 5 == 0 )); then echo "loop"
        else echo $i;
        fi
done


################################
echo
sleep 2
################################


################
# while loop-1 #
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

################################
echo
sleep 2
################################

################
# while loop-2 #
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
