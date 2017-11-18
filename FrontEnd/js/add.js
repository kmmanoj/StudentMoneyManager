function add()
{
  date = document.getElementById("date");
  type = document.getElementById("type"); //dropdown
  type_value = type.options[type.selectedIndex].text;

  category = document.getElementById("category"); //dropdown
  category_value = category.options[category.selectedIndex].text;

  dealer = document.getElementById("dealer");
  if(document.getElementById("paid_status").checked)
    paid_status_value = true;
  else
    paid_status_value = false;

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
  
  xhr.open("POST", "send.php", true);
  xhr.setRequestHeader("Content-type", "application/json");
  obj2 = JSON.stringify(obj1);
  xhr.send(obj2);

}

function result()
{
  div1 = document.getElementById("result");

  if(this.readyState == 4 && this.status == 200)
  {
    jsonObj = JSON.parse(this.responseText);
    if(jsonObj.error == null)
    {
      if(jsonObj.response.status)
      { 
        t = document.createTextNode("Added Transaction Successfully!");
      }
      else
        t = document.createTextNode("Unsuccessful transaction!");
    }
   
  
    h3 = document.createElement("h3");
    h3.appendChild(t);
    div1.appendChild(h3);
  }
}