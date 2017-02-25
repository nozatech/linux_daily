<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>Switch</title>
        </head>
        <body>

        <?php
          echo "if a is 3,  <br />";

          $a = 9;
          switch ($a) {
            case 0:
              echo "a equals 0 <br />";
                break;
            case 1:
              echo "a equals 1 <br />";
                break;
            case 2:
              echo "a equals 2 <br />";
                break;
            case 3:
              echo "a equals 3 <br />";
                break;
            default:
              echo " a is none of above<br />";
                break;
        }
        ?>

        <?php
        $year = 2013;
        switch (($year - 4) % 12) {  //modulo of 12//
                case 0:  $zodiac = 'RAT';       break;
                case 1:  $zodiac = 'Ox';        break;
                case 2:  $zodiac = 'Tiger';     break;
                case 3:  $zodiac = 'Rabbit';    break;
                case 4:  $zodiac = 'Dragon';    break;
                case 5:  $zodiac = 'Snake';     break;
                case 6:  $zodiac = 'Horse';     break;
                case 7:  $zodiac = 'sheep';      break;
                case 8:  $zodiac = 'Monkey';    break;
                case 9:  $zodiac = 'Chicken';   break;
                case 10: $zodiac = 'Dog';       break;
                case 11: $zodiac = 'Pig';       break;
        }
        echo "{$year} is the year of the {$zodiac}.<br />";
        ?>

		<?php
          $user_type = 'customer';

          switch ($user_type) {

            case 'student';
                echo "Welcome";
                break;
            case 'press';
                echo "Greetings!";
                break;
            case 'customer';
                echo "Hello!";
                break;
          }
        ?>



        </body>
</html>

<!--
if a set to 0(zero) without break, then result wil be
display all matches after first match.

a equals 0
a equals 1
"switch.php" 69L, 1330C written                                             49,50-57      Top
-->