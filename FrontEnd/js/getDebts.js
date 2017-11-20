function getAll()
{
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = displayDetails;
	xhr.open("GET", "getDebts.php", true);
	xhr.send();

}