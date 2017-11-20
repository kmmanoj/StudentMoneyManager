function getAll()
{
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = displayDetails;
	xhr.open("GET", "getOwes.php", true);
	xhr.send();

}