function update()
{
  date = document.getElementById("date");
  type = document.getElementById("type"); //dropdown
  type_value = type.options[type.selectedIndex].text;
  id = document.getElementById("id");
  //window.alert(type_value);

  category = document.getElementById("category"); //dropdown
  category_value = category.options[category.selectedIndex].text;

  dealer = document.getElementById("dealer");
  //paid_status = document.getElementById("paid_status"); //checkbox
  if(document.getElementById("paid_status").checked)
    paid_status_value = true;
  else
    paid_status_value = false;

  //window.alert(paid_status_value);

  amount = document.getElementById("amount");
  
  obj1 = 
  {
    id : id.value,
    date : date.value,
    type: type_value,
    category : category_value,
    dealer : dealer.value,
    paid_status : paid_status_value,
    amount : amount.value
  }
  xhr1 = new XMLHttpRequest();
  xhr1.onreadystatechange = result; 
  xhr1.open("POST", "update.php", true);
  xhr1.setRequestHeader("Content-type", "application/json");
  //obj1 = JSON.stringify({name : name.value, dob: dob.value, username : uname.value, password : pwd.value});
  obj2 = JSON.stringify(obj1);
  xhr1.send(obj2);

}

function result()
{
  div1 = document.getElementById("result");
  if(xhr1.readyState == 4 && xhr1.status == 200)
  {
 
    jsonObj = JSON.parse(xhr.response);
    //window.alert(jsonObj.status);
    if(jsonObj.error == null)
    {
      if(jsonObj.response.status)
      { 
        t = document.createTextNode("Updated Transaction Successfully!");
      }
      else
        t = document.createTextNode("Unsuccessful Updation!");
    }
    
    h3 = document.createElement("h3");
    h3.appendChild(t);
    div1.appendChild(h3);
  }
}


function displayDetails()
{
  if(xhr2.readyState == 4 && xhr2.status == 200)
  {
    //window.alert(xhr2.reponseText);
    // jsonObj = JSON.parse(xhr2.reponse);
    // if(jsonObj.error == null)
    // {
    //   date.value = jsonObj.data.date;
    //   //type
    //   //category
    //   dealer.value = jsonObj.data.dealer;
    //   if(jsonObj.data.paid_status)
    //     document.getElementById("paid_status").checked = true;
    //   else
    //     document.getElementById("paid_status").checked = false;
    //   amount.value = jsonObj.data.amount;
    // }
    // else
    // {
    //   div1 = document.getElementById("result");
    //   t = document.createTextNode("Failed to update results");
    //   h3 = document.createElement("h3");
    //   h3.appendChild(t);
    //   div1.appendChild(h3);
    // }

  }
}