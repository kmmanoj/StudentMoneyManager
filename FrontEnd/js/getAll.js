function getAll()
{
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = displayDetails;
	xhr2.open("GET", "getAll.php", true);
	xhr2.send();

}