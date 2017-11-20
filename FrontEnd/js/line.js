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

	xhr2 = new XMLHttpRequest();
	xhr2.onreadystatechange = saveLine; 
	xhr2.open("GET", "line.php?type=save",true);
	xhr2.send();
}

function creditLine()
{
	if(this.readyState == 4 && this.status ==200)
	{
		jsonObj = JSON.parse(this.responseText);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				var data = new google.visualization.DataTable();
				data.addColumn('string', 'Date');
				data.addColumn('number', 'Credit');
				for(var i=0; i<jsonObj.response.data.length; i++)
				{
					obj1 = jsonObj.response.data[i];
					data.addRow([obj1.date, obj1.amount]);
				}

				var options = {'title' : 'Credit Expenditure Recorded',
               hAxis: {
                  title: 'Date'
               },
               vAxis: {
                  title: 'Credit Amount'
               },   
               'width':900,
               'height':500,
               curveType: 'function'
            };

            var chart = new google.visualization.LineChart(document.getElementById('chart1'));
            chart.draw(data, options);
            google.charts.setOnLoadCallback();
			}
		}
	}
}

function debitLine()
{
	if(this.readyState == 4 && this.status ==200)
	{
		jsonObj = JSON.parse(this.responseText);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				var data = new google.visualization.DataTable();
				data.addColumn('string', 'Date');
				data.addColumn('number', 'Debit');
				for(var i=0; i<jsonObj.response.data.length; i++)
				{
					obj1 = jsonObj.response.data[i];
					data.addRow([obj1.date, obj1.amount]);
				}

				var options = {'title' : 'Debit Recorded',
               hAxis: {
                  title: 'Date'
               },
               vAxis: {
                  title: 'Debit Amount'
               },   
               'width':900,
               'height':500,
               colors: ['#c71585'],
               curveType: 'function'
            };

            var chart = new google.visualization.LineChart(document.getElementById('chart2'));
            chart.draw(data, options);
            google.charts.setOnLoadCallback();
			}
		}
	}
}

function saveLine()
{
	if(this.readyState == 4 && this.status ==200)
	{
		jsonObj = JSON.parse(this.responseText);
		if(jsonObj.error == null)
		{
			if(jsonObj.status)
			{
				var data = new google.visualization.DataTable();
				data.addColumn('string', 'Date');
				data.addColumn('number', 'Save');
				for(var i=0; i<jsonObj.response.data.length; i++)
				{
					obj1 = jsonObj.response.data[i];
					data.addRow([obj1.date, obj1.amount]);
				}

				var options = {'title' : 'Savings Recorded',
               hAxis: {
                  title: 'Date'
               },
               vAxis: {
                  title: 'Save Amount'
               },   
               'width':900,
               'height':500,
               colors: ['#228b22'],
               curveType: 'function'
            };

            var chart = new google.visualization.LineChart(document.getElementById('chart3'));
            chart.draw(data, options);
            google.charts.setOnLoadCallback();
			}
		}
	}
}