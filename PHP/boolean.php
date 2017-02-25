<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>Booleans</title>
        </head>
        <body>

        <?php
        $result1 = true;
        $result2 = false;


        ?>
        Resutl1: <?php echo $result1; ?><br />
        Result2: <?php echo $result2; ?><br />

        Result1 is boolean? <?php echo is_bool($result1); ?><br />
        Result2 is boolean? <?php echo is_bool($result2); ?><br />


        <?php
          $number = 3.14;
          if(is_float($number)) {
                echo "It is a float.";
          }
        ?>
        </body>
</html>

<--

Resutl1: 1
Result2:
Result1 is boolean? 1
Result2 is boolean? 1
It is a float.

-->
