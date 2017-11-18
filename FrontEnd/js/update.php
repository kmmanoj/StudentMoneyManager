<?php
session_start();
header("Content-type:application/json");

$data = file_get_contents("php://input");
$send = json_encode($data);
$temp = json_decode($data, true);

//echo $temp['id'];
$uname   = $_SESSION['uname'];
$header  = array("User:$uname", "Content-type:application/json");
$request = array('http' => array('method' => "POST", 'header' => $header, 'content' => $data));
$context = stream_context_create($request);
$retval  = file_get_contents("http://localhost:5000/transactions/edit/".$temp['id'], FALSE, $context);
echo $retval;
?>
