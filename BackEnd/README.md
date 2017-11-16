<h3>GET /</h3>
<fieldset>
<p>response</p>
<pre>
{
	connection : string
}
</pre>
<hr/>

<h3>GET /auth/&lt;username&gt;/&lt;password&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		name : string,
		username : string,
		authenticate : boolean
	}
}
</pre>
<hr/>

<h3>POST /register</h3>
<p>request</p>
<pre>
{
	name : string,
	dob : date,
	username : string,
	password : string
}
</pre>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : {
		status : boolean
	}
}
</pre>
<hr/>

<h3>GET /user/&lt;username&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		exists: boolean
	}
}
</pre>
<hr/>

<h3>GET /transactions/all/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				type : string,
				category : string,
				dealer : string,
				paid_status : boolean,
				amount : int
			}
		])
	}
}
</pre>
<hr/>

<h3>POST /transactions/add</h3>
<p>request</p>
<pre>
{
	date : date,
	type : string,
	category : string,
	dealer : string,
	paid_status : boolean,
	amount : int
}
</pre>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		status : boolean
	}
}
</pre>
<hr/>

<h3>GET /transactions/delete/&lt;doc_id&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		status : boolean
	}
}
</pre>
<hr/>

<h3>GET /transactions/id/&lt;doc_id&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :{
		data:
		{
			date : date,
			type : string,
			category : string,
			dealer : string,
			paid_status : boolean,
			amount : int
		}
	}
}
</pre>
<hr/>

<h3>POST /transactions/edit/&lt;doc_id&gt;</h3>
<p>request</p>
<pre>
{
	date : date,
	type : string, 
	category : string,
	dealer : string,
	paid_status : boolean,
	amount : int
}
</pre>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		status : boolean
	}
}
</pre>
<hr/>

<h3>GET /debts/all/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				category : string,
				dealer : string,
				amount : int
			}
		])	
	}
}
</pre>
<hr/>

<h3>POST /debts/update</h3>
<p>request</p>
<pre>
{
	id : array([ string ])
}
</pre>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		count : int
	}
}
</pre>
<hr/>


<h3>GET /owes/all/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				category : string,
				dealer : string,
				amount : int
			}
		])	
	}
}
</pre>
<hr/>


<h3>POST /owes/update</h3>
<p>request</p>
<pre>
{
	id : array([ string ])
}
</pre>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		count : int
	}
}
</pre>
<hr/>

<h3>GET /categories/all</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response : 
	{
		data : array([ string ])
	}
}
</pre>
<hr/>

<h3>GET /summary/category</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data :
		{
			<i>category_1</i> :
			{
				expense : int
			} 
			...
			<i>category_n</i> :
			{
				expense : int
			}
		}
	}
}
</pre>
<hr/>

<h3>GET /summary/weekdays</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		{
			sunday :
			{
				credit : int,
				debit : int,
				save : int
			}
			...
			saturday :
			{
				credit : int,
				debit : int,
				save : int
			}
		}
	}
}
</pre>
<hr/>


<h3>GET /transactions/type/credit/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				category : string,
				dealer : string,
				amount : int
			}
		])
	}
}
</pre>
<hr/>

<h3>GET /transactions/type/debit/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				category : string,
				dealer : string,
				amount : int
			}
		])
	}
}
</pre>
<hr/>

<h3>GET /transactions/type/save/&lt;offset&gt;/&lt;limit&gt;</h3>
<p>response</p>
<pre>
{
	status : int,
	error : string,
	response :
	{
		data : 
		array([
			{
				date : date,
				category : string,
				dealer : string,
				amount : int
			}
		])
	}
}
</pre>
<hr/>
