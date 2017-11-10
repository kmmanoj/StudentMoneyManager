<h3>GET /</h3>
<fieldset>
	<legend>response</legend>
	<pre>
	{
		connection : success
	}
	</pre>
</fieldset>
<hr/>
<h3>GET /auth/&gt;username&lt;/&gt;password&lt;</h3>
<fieldset>
	<legend>response</legend>
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
</fieldset>
<hr/>
<h3>POST /register</h3>
<fieldset>
	<legend>request</legend>
	<pre>
		{
			name : string,
			dob : date,
			username : string,
			password : string
		}
	</pre>
</fieldset>
<fieldset>
	<legend>response</legend>
	<pre>
		{
			status : int,
			error : string,
			response : {
				status : boolean
			}
		}
	</pre>
</fieldset>
<hr/>

