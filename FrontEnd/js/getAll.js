function getAll()
{
	window.alert("Came to getAll");
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = displayDetails;
	xhr.open("GET", "getAll.php", true);
	xhr.send();

}