<?php
session_start();
?>
<!DOCTYPE html>
<html>
    <head>
        <title>Line graph</title>
    </head>
    <body>
        <button onclick="by_weekdays">Weekdays</button><br/>
        <button onclick="by_category">Category</button><br/>
        <!-- use google charts API -->
        <canvas height="200" width="200" style="border:1px solid black"></canvas>
    </body>
</html>