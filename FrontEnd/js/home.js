function displayDetails()
{
	
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(this.responseText);
		console.log(jsonObj);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				tab1 = document.getElementById("tab1");
				for(var i=0; i<jsonObj.response.data.length; i++)
				{
					obj1 = jsonObj.response.data[i];
					tr1 = tab1.insertRow(i+1);
					
					cell1 = tr1.insertCell(0);
					cell1.innerHTML = obj1.date;

					cell2 = tr1.insertCell(1);
					cell2.innerHTML = obj1.type;

					cell3 = tr1.insertCell(2);
					cell3.innerHTML = obj1.category;

					cell4 = tr1.insertCell(3);
					cell4.innerHTML = obj1.dealer;

					cell5 = tr1.insertCell(4);
					cbx2 = document.createElement("input");
					cbx2.type="checkbox";
					cbx2.disabled=true;
					
					if(obj1.paid_status=="true"){
						cbx2.checked=true;
						cell5.appendChild(cbx2);
					}
					else if(obj1.paid_status=="false"){
						cbx2.checked=false;
						cell5.appendChild(cbx2);
					}

					cell6 = tr1.insertCell(5);
					cell6.innerHTML = obj1.amount;
				}
			}
		}

	}
}