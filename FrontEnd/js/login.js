function login()
{
	uname = document.getElementById("logUname");
	pwd = document.getElementById("logPwd");
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = loginResult; 
	var url = "http://localhost:5000/auth/" +uname.value+"/"+pwd.value;
	//window.alert(url);
	xhr.open("GET", url, true);
	xhr.send();
}
function loginResult()
{
	loginDiv = document.getElementById("loginDiv");
	loginDiv.innerHTML = "";
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(xhr.responseText);
    console.log(jsonObj);
		if(jsonObj.response.authenticate)
		{
			t = document.createTextNode("Logged in Successfully!");
			//start session and create php session variable
			xhr = new XMLHttpRequest();
			xhr.onreadystatechange = startSesh;
			xhr.open("GET", "startSesh.php?uname="+uname.value, true);
		  	xhr.setRequestHeader("username", uname.value);
			xhr.send();

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
		//window.alert(this.reponse);
    	//redirect to another page --> home.php
    	window.location.href
	}
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
	//window.alert(rname.value);
	uname = document.getElementById("regUname");
	//window.alert(uname.value);
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
		//xhr.open("GET", "authenticate.php?uname="+uname, true);
		xhr.open("POST", "http://localhost:5000/register", true);
		xhr.setRequestHeader("Content-type", "application/json");
		//obj1 = JSON.stringify({name : name.value, dob: dob.value, username : uname.value, password : pwd.value});
		obj2 = JSON.stringify(obj1);
    //window.alert(obj2);
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