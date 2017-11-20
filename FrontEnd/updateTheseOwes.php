<?php
session_start();
header('Location:home.php');
$id_list = array();
parse_str(file_get_contents("php://input"), $id_list);
$return_json = array();
$count       = 0;

unset($id_list['delete']);
foreach ($id_list as $id => $value) {

	$request_url    = "http://localhost:5000/owes/update/$id";
	$request_method = "GET";

	header("Content-type:application/json");
	$data      = json_encode(file_get_contents("php://input"));
	$uname     = $_SESSION['uname'];
	$header    = array("User:$uname", "Content-type:application/json");
	$request   = array('http' => array('method' => $request_method, 'header' => $header, 'content' => $data));
	$context   = stream_context_create($request);
	$retval    = file_get_contents($request_url, FALSE, $context);
	$ret_assoc = json_decode($retval, true);

	if ($ret_assoc['response']['status']) {
		$count += 1;
	}
}

exit();
?>