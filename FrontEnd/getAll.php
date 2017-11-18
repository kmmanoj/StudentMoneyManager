<?php
session_start();

$request_url    = "http://localhost:5000/transactions/all/0/1000";
$request_method = "GET";

header("Content-type:application/json");
$data    = json_encode(file_get_contents("php://input"));
$uname   = $_SESSION['uname'];
$header  = array("User:$uname", "Content-type:application/json");
$request = array('http' => array('method' => $request_method, 'header' => $header, 'content' => $data));
$context = stream_context_create($request);
$retval  = file_get_contents($request_url, FALSE, $context);
echo ($retval);
?>
