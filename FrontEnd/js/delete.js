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
					
					cell0 = tr1.insertCell(0);

					cbx = document.createElement("input");
					cbx.type = "checkbox";
					cbx.id = obj1._id.$oid;
					cbx.name = cbx.id;

					cell0.appendChild(cbx); 

					cell1 = tr1.insertCell(1);
					cell1.innerHTML = obj1.date;

					cell2 = tr1.insertCell(2);
					cell2.innerHTML = obj1.type;

					cell3 = tr1.insertCell(3);
					cell3.innerHTML = obj1.category;

					cell4 = tr1.insertCell(4);
					cell4.innerHTML = obj1.dealer;

					cell5 = tr1.insertCell(5);
					cbx2 = document.createElement("input");
					cbx2.type="checkbox";
					cbx2.disabled=true;
					
					if(obj1.paid_status)
						cbx2.checked=true;
					else
						cbx2.checked=false;
					cell5.appendChild(cbx2);

					cell6 = tr1.insertCell(6);
					cell6.innerHTML = obj1.amount;
				}
			}
		}

	}
}