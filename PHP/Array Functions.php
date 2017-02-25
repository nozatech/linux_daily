<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
  <head>
    <title>Array Functions</title>
  </head>
  <body>
    <?php $numbers = array(8,23,15,42,16,4); ?>

    Count:      <?php echo count($numbers); ?><br />
    Max value   <?php echo max($numbers);   ?><br />
    Min Value   <?php echo min($numbers);   ?><br />
    <br />

    <pre>
    Sort:         <?php sort($numbers); print_r($numbers); ?><br />
    Reverse sort: <?php rsort($numbers); print_r($numbers); ?><br />
    </pre>


    Implode(change to string):
                <?php echo $num_string = implode(" * ", $numbers); ?><br />

    Explode(change to ):
                <?php print_r(explode(" * ", $num_string)); ?><br />

    15 in array?: <?php echo in_array(15, $numbers); //Returns True/False ?><br />
    19 in array?: <?php echo in_array(19, $numbers); //returns T=1 /F=0   ?><br />
    Note:  1 = True / 0 = False







  </body>
</html>


<!--                <= Comment!

Count:  6
Max value       42
Min Value       4

Sort:   Array ( [0] => 4 [1] => 8 [2] => 15 [3] => 16 [4] => 23 [5] => 42 )
Reverse sort: Array ( [0] => 42 [1] => 23 [2] => 16 [3] => 15 [4] => 8 [5] => 4 )


if use
<pre>  </pre>
    Sort:       Array
(
    [0] => 4
    [1] => 8
    [2] => 15
    [3] => 16
    [4] => 23
    [5] => 42
)

    Reverse sort: Array
(
    [0] => 42
    [1] => 23
    [2] => 16
    [3] => 15
    [4] => 8
    [5] => 4
)

Implode(change to string):      42 * 23 * 16 * 15 * 8 * 4
Explode(change to ): Array ( [0] => 42 [1] => 23 [2] => 16 [3] => 15 [4] => 8 [5] => 4 )





-->
