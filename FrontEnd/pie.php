<?php
	session_start();
	extract($_GET);
	$url = "http://localhost:5000/summary/".$category;
	$method = "GET";
	header("Content-type:application/json");
	$data    = json_encode(file_get_contents("php://input"));
	$uname   = $_SESSION['uname'];
	$header  = array("User:$uname", "Content-type:application/json");
	$request = array('http' => array('method' => $method, 'header' => $header, 'content' => $data));
	$context = stream_context_create($request);
	$retval  = file_get_contents($url, FALSE, $context);
	echo ($retval);
?>