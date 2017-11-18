<?php
session_start();

extract($_GET);

$uname   = $_SESSION['uname'];
$header  = array("User:$uname", "Content-type:application/json");
$request = array('http' => array('method' => "GET", 'header' => $header));
$context = stream_context_create($request);
$retval  = file_get_contents("https://localhost:5000/transactions/id/".$_GET['id'], FALSE, $context);
echo $retval;
?>
