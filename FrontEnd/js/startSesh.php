<?php
	session_start();
	extract($_GET);
	header("Access-Control-Allow-Origin: *");
	
	$_SESSION['uname']=$uname;

	echo $uname;
?php>