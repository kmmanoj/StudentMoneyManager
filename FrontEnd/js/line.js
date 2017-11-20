function getLine()
{
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = creditLine; 
	xhr.open("GET", "line.php?type=credit",true);
	xhr.send();

	xhr1 = new XMLHttpRequest();
	xhr1.onreadystatechange = debitLine; 
	xhr1.open("GET", "line.php?type=debit",true);
	xhr1.send();

xhr = new XMLHttpRequest();
	xhr.onreadystatechange = saveDisplay; 
	xhr.open("GET", "line.php?type=save",true);
	xhr.send();
}