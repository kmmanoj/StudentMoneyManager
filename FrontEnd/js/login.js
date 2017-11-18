function login()
{
	uname = document.getElementById("logUname");
	pwd = document.getElementById("logPwd");
	xhr1 = new XMLHttpRequest();
	xhr1.onreadystatechange = loginResult; 
	var url = "http://localhost:5000/auth/" +uname.value+"/"+pwd.value;
	//url = "authenticate.php?uname=" +uname.value+"&pwd="+pwd.value; 
	xhr1.open("GET", url, true);
	xhr1.send();
}
function loginResult()
{
	loginDiv = document.getElementById("loginDiv");
	loginDiv.innerHTML = "";
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(xhr1.responseText);
    	console.log(jsonObj);
		if(jsonObj.response.authenticate)
		{
			t = document.createTextNode("Logged in Successfully!");
			//start session and create php session variable
			xhr2 = new XMLHttpRequest();
			xhr2.onreadystatechange = startSesh;
			
			xhr2.open("GET", "startSesh.php?uname="+uname.value, true);
			xhr2.send();

		}
		else
		{
		 	t = document.createTextNode("Login not successful :(");
		}
		
		h2 = document.createElement("h2");
		h2.appendChild(t);
		loginDiv.append(h2);
	}
}
function startSesh()
{
	if(this.readyState == 4 && this.status == 200)
	{
		//console.log(this.responseText);
		//add delay of 3 seconds
		h3 = document.createElement("h3");
    	t = document.createTextNode("Redirecting...");
    	h3.appendChild(t);
    	loginDiv.append(h3);

		setTimeout(redirect, 3000);
    	
    	
	}
}
function redirect()
{
	window.location.href = "home.php";
}
function check()
{
	if (document.getElementById('regPwd').value ==
    document.getElementById('regPwd2').value) 
    {
    	document.getElementById('message').style.color = 'green';
    	document.getElementById('message').innerHTML = 'Passwords Match';
  	} 
  	else 
  	{
    	document.getElementById('message').style.color = 'red';
    	document.getElementById('message').innerHTML = "Passwords Don't Match";

	}
}
function register()
{
	rname = document.getElementById("regName");
	uname = document.getElementById("regUname");
	pwd = document.getElementById("regPwd");
	pwd2 = document.getElementById("regPwd2");
	dob = document.getElementById("dob");

	if(pwd.value == pwd2.value)
	{
		obj1 = 
		{
			name : rname.value,
			dob: dob.value,
			username : uname.value,
			password : pwd.value
		}

		xhr = new XMLHttpRequest();
		xhr.onreadystatechange = resultDisplay; 
		xhr.open("POST", "register.php", true);
		xhr.setRequestHeader("Content-type", "application/json");
		obj2 = JSON.stringify(obj1);
		xhr.send(obj2);
	}
	else
	{
		window.alert("Passwords don't match!");
	}
}

function resultDisplay()
{
	div1 = document.getElementById("displayRes");
	h1 = document.createElement("H1");
	div1.innerHTML = " ";
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(this.responseText);
		if(jsonObj.response.status == true)
		{
			t = document.createTextNode("Registered Successfully!");
		}
		else
		{
			//throw error in page
			t = document.createTextNode(jsonObj.error);
		}
		h1.appendChild(t);
		div1.append(h1);
	}
}