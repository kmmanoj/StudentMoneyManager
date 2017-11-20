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
					cell2.innerHTML = obj1.dealer;

					cell3 = tr1.insertCell(3);
					cell3.innerHTML = obj1.amount;
				}
			}
		}

	}
}