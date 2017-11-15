function add()
{
  date = document.getElementById("date");
  type = document.getElementById("type"); //dropdown
  type_value = type.options[type.selectedIndex].text;
  //window.alert(type_value);

  category = document.getElementById("category"); //dropdown
  category_value = category.options[category.selectedIndex].text;

  dealer = document.getElementById("dealer");
  //paid_status = document.getElementById("paid_status"); //checkbox
  if(document.getElementById("paid_status").checked)
    paid_status_value = true;
  else
    paid_status_value = false;

  window.alert(paid_status_value);

  amount = document.getElementById("amount");
  
  obj1 = 
  {
    date : date.value,
    type: type_value,
    category : category_value,
    dealer : dealer.value,
    paid_status : paid_status_value,
    amount : amount.value
  }
  xhr = new XMLHttpRequest();
  xhr.onreadystatechange = result; 
  //xhr.open("GET", "authenticate.php?uname="+uname, true);
  //make this php file
  //in php file extract post, add header to request and send using file_get_contents
  //add header using http_...
  //header: username = $_uname
  xhr.open("POST", "http://localhost:5000/transactions/add", true);
  xhr.setRequestHeader("Content-type", "application/json");
  //obj1 = JSON.stringify({name : name.value, dob: dob.value, username : uname.value, password : pwd.value});
  obj2 = JSON.stringify(obj1);
  xhr.send(obj2);

}

function result()
{
  div1 = document.getElementById("result");

  if(this.readyState == 4 && this.status == 200)
  {
    jsonObj = JSON.parse(this.responseText);
    if(jsonObj.status == 1) //ask
    {
      t = document.createTextNode("Added Transaction Successfully!");
    }
    else
    {
      t = document.createTextNode(jsonObj.error);
    }
  
    h3 = document.createElement("h3");
    h3.appendChild(t);
    div1.appendChild(h3);
  }
}