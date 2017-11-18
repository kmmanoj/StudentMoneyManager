<?php
session_start();
//header('Location:home.php');
$data = array();
parse_str(file_get_contents("php://input"), $data);
var_dump($data);
$id = $data['id'];
unset($data['id']);
$request_url    = "http://localhost:5000/transactions/edit/$id";
$request_method = "POST";
header("Content-type:application/json");
$data = json_encode($data, true);
echo ($data);
$uname   = $_SESSION['uname'];
$header  = array("User:$uname", "Content-type:application/json");
$request = array('http' => array('method' => $request_method, 'header' => $header, 'content' => $data));
$context = stream_context_create($request);
$retval  = file_get_contents($request_url, FALSE, $context);
?>
