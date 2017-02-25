<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>Null and empty</title>
        </head>
        <body>

        <?php
        $var1 = null;
        $var2 ="";
        ?>
        var1 null? <?php echo is_null($var1); ?><br />
        var2 null? <?php echo is_null($var2); ?><br />
        var3 null? <?php echo is_null($var3); ?><br />
        <br />
        var1 null? <?php echo isset($var1); ?><br />
        var2 null? <?php echo isset($var2); ?><br />
        var3 null? <?php echo isset($var3); ?><br />
        <br />

        <?php // comment- empty: "", null, 0, 0.0, "0", false, array() ?>

        <?php $var3 = "0"; ?>

        var1 empty? <?php echo empty($var1); ?><br />
        var2 empty? <?php echo empty($var2); ?><br />
        var3 empty? <?php echo empty($var3); ?><br />



        </body>
</html>

<!--
blank submit form EMPTY! cause a lot of bugs!
var1 null? 1
var2 null?
var3 null? 1

var1 null?
var2 null? 1
var3 null?

var1 empty? 1
var2 empty? 1
var3 empty? 1


-->
