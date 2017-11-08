<pre>
login():
	{ username, auth_token }
	{ key }
	where key : E(key+cookie, password)
	and auth_token : E(username+TS, password)
	Cipher text = Encryption(text, key)
register():
	{ username, name, password , birth_date }
	{ status }
	where password : E(password, server_public_key)
get_transactions():
	{ cookie, offset, limit }
	{ data }
	where cookie : E(cookie+TS, key)
add_transaction():
	{ cookie, date, type, category, dealer, paid }
	{ status }
delete_transaction():
	{ cookie, id }
	{ status }
get_transaction():
	{ cookie, id }
	{ data }
update_transaction():
	{ cookie, data }
	{ status }
get_debt_list():
	{ cookie, offset, limit }
	{ data }
debt_update():
	{ cookie, id_list }
	{ status }
get_owe_list():
	{ cookie, offset, limit }
	{ data }
owe_update():
	{ cookie, id_list }
	{ status }

get_all_unique_categories():
	{ cookie }
	{ data }

get_week_summary():
	{ cookie }
	{ data }
get_category_summary():
	{ cookie }
	{ data }
get_credit_transactions():
	{ cookie, offset, limit }
	{ data }
get_debit_transactions():
	{ cookie, offset, limit }
	{ data }
get_saved_transactions():
	{ cookie, offset, limit }
	{ data }
</pre>
