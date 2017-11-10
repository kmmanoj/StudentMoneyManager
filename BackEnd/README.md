<h3>GET /</h3>
<fieldset>
<p>response</p>
<pre>
{
	connection : success
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

<h3>POST /register</h3>
<p>request</p>
<pre>
{

}
</pre>
<p>response</p>
<pre>
{

}
</pre>
<hr/>


