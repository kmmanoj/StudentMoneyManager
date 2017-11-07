login(username, password):
	{ auth_token }
	{ key }
	where key : E(key+cookie, password)
	and auth_token : E(username+TS, password)
	Cipher text = Encryption(text, key)
register(data):
	{ username, name, password , birth_date }
	{ status }
	where password : E(password, server_public_key)
get_transactions(offset, limit):
	{ cookie, offset, limit }
	{ data }
	where cookie : E(cookie+TS, key)
add_transaction(data):
	{ cookie, date, type, category, dealer, paid }
	{ status }
delete_transaction(data):
	{ cookie, id }
	{ status }
get_transaction(id):
	{ cookie, id }
	{ data }
update_transaction(data):
	{ cookie, data }
	{ status }
get_debt_list(offset, limit):
	{ cookie, offset, limit }
	{ data }
debt_update(id_list):
	{ cookie, id_list }
	{ status }
get_owe_list(offset, limit):
	{ cookie, offset, limit }
	{ data }
owe_update(id_list):
	{ cookie, id_list }
	{ status }

get_all_unique_categories():
	{ cookie }
	{ data }

// some more to be added .. that are specific to pie chart and line graphs
