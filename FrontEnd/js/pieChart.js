function getChart()
{
	xhr = new XMLHttpRequest();
	xhr.onreadystatechange = catChart; 
	xhr.open("GET", "pie.php?category=category",true);
	xhr.send();

	xhr1 = new XMLHttpRequest();
	xhr1.onreadystatechange = weekChart; 
	xhr1.open("GET", "pie.php?category=weekdays",true);
	xhr1.send();
}

function catChart()
{
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(this.responseText);
		console.log(jsonObj);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				var data = new google.visualization.DataTable();
				data.addColumn('string', 'Category');
				data.addColumn('number', 'Expense');
				for(var i in jsonObj.response.data)
				{
					
					if(jsonObj.response.data[i].expense < 0)
						jsonObj.response.data[i].expense *= -1;
					data.addRow([i, jsonObj.response.data[i].expense]);
					
				}
				
				//console.log(data);
				var options = {
          			title: 'Expenses Category Wise',
          			legend: { position: 'top', maxLines: 6 },
          			sliceVisibilityThreshold: 0,
          			width : 600,
          			height : 600
        		};

        		var chart = new google.visualization.PieChart(document.getElementById('chart1'));
        		chart.draw(data, options);

			}
		}
	}
}

function weekChart()
{
	if(this.readyState == 4 && this.status == 200)
	{
		jsonObj = JSON.parse(this.responseText);
		console.log(jsonObj);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				var data = new google.visualization.DataTable();
				data.addColumn('string', 'Weekday');
				data.addColumn('number', 'Expense');
				for(var i in jsonObj.response.data)
				{
					if(jsonObj.response.data[i].actual<0)
						jsonObj.response.data[i].actual*=-1;

					data.addRow([i, jsonObj.response.data[i].actual]);
					
				}
				console.log(data);
				var options = {
          			title: 'Expenses Day Wise',
          			legend: { position: 'top', maxLines: 6 },
          			sliceVisibilityThreshold: 0,
          			width : 600,
          			height : 600
        		};

        		var chart = new google.visualization.PieChart(document.getElementById('chart2'));
        		chart.draw(data, options);

			}
		}
	}
}