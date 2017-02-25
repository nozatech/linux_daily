<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>IF statement</title>
        </head>
        <body>

        Case1: a = 4, b = 3 <br />
        <?php
          $a = 4;
          $b = 3;

          if ($a > $b) {
            echo "Yes, a is larger than b";
          }
          ?>
        <br />


        Case2: a = 3, b = 4 <br />

        <?php
          $a = 3;
          $b = 4;

          if ($a > $b) {
                echo "yes, a is larger than b";
          }
        ?>

        <br />

        <?php //Only welcome new users
          $new_user = true;
          if ($new_user) {
                echo "<h1>Welcome</h1>";
                echo "<p>Join us!</p>";
          }

        ?>
        <br />

        <?php //don't divide by zero
          $numerator = 20;
          $denominator = 4;
          if ($denominator > 0) {
                $result = $numerator / $denominator;
                echo "20 divided by 4 is {$result}";
          }
        ?>






        </body>
</html>
~
~
~
"if_statement.php" 60L, 818C written                                        50,28-40      All
