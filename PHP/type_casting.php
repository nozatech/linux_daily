<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>type juggling & casting</title>
        </head>
        <body>

        Type Juggling<br />
        <?php $count = "2 cats"; //string// ?>
        Type: <?php echo gettype($count); ?><br />


        <?php $count +=3; //add integer 3// ?>
        Type: <?php echo gettype($count); ?><br />

        <?php $cats = "I have " . $count . " cats."; //string integer <=juggles back// ?>
        Cats: <?php echo gettype($cats); ?><br />

        <br />

        Type Casting<br />
        <?php settype($count, "integer"); //string// ?>
        Count: <?php echo gettype($count); //switch to integer// ?><br />
        <br />

        <?php $count2 = (string) $count; ?>
        count1: <?php echo gettype($count); ?><br />
        count2: <?php echo gettype($count2); ?><br />
        <br />

        <?php $test1 = 3; ?>
        <?php $test2 = 3; ?>
        <?php settype($test1, "string"); ?>
        <?php (string) $test2; ?>
        test1: <?php echo gettype($test1); ?><br />
        test2: <?php echo gettype($test2); ?><br />




        </body>
</html>
