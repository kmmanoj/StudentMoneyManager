<?php
session_start();
header("Content-type:application/json");
$data = json_encode(file_get_contents("php://input"));

$uname   = $_SESSION['uname'];
$header  = array("User:$uname", "Content-type:application/json");
$request = array('http' => array('method' => "POST", 'header' => $header, 'content' => $data));
$context = stream_context_create($request);
$retval  = file_get_contents("http://localhost:5000/transactions/add", FALSE, $context);
echo ($retval);
?>
