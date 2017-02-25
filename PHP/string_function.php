<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
        "http://www.w3.org/TR/html4/loose.dtd">

<html lang="en">
        <head>
                <title>basic php</title>
        </head>
        <body>
        <?php
        $first = "The quick brown fox";
        $second = " jumped over the lazy dog.";

        $third = $first;
        $third .= $second;
//  . is concatenate the second.  Adding first + second
        echo $third;
        ?>
        <br />

        Lowercase: <?php echo strtolower($third); ?><br />
<!-- Lowering case htmp function # string to lower -->
        Uppercase: <?php echo strtoupper($third); ?><br />
        Uppercase first: <?php echo ucfirst($third); ?><br />
<!-- Uppercase only first word -->
        Uppercase words: <?php echo ucwords($third); ?><br />
<!-- Uppercase each word -->

        <br />
        Length: <?php echo strlen($third); ?><br />
        Trim: <?php echo "A" . trim(" B C D ") . "E"; ?><br />
        Find: <?php echo strstr($third, "brown"); ?><br />
        Replace by string: <?php echo str_replace("quick", "supper-fast", $third); ?><br />
        <br />
        Repeat: <?php echo str_repeat($third, 2); ?><br />
        Make substring: <?php echo substr($third, 5, 10); ?><br />
        Find position: <?php echo strpos($third, "brown"); ?><br />
        Find character: <?php echo strchr($third, "z"); ?><br />



        </body>
</html>

<!--
The quick brown fox jumped over the lazy dog.	
Lowercase: the quick brown fox jumped over the lazy dog.
Uppercase: THE QUICK BROWN FOX JUMPED OVER THE LAZY DOG.
Uppercase first: The quick brown fox jumped over the lazy dog.
Uppercase words: The Quick Brown Fox Jumped Over The Lazy Dog.

Length: 45
Trim: AB C DE
Find: brown fox jumped over the lazy dog.
Replace by string: The supper-fast brown fox jumped over the lazy dog.

Repeat: The quick brown fox jumped over the lazy dog.The quick brown fox jumped over the lazy dog.
Make substring: uick brown
Find position: 10
Find character: zy dog.
-->