'''
WEB SERVICE APIs

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
from flask import Flask, request
import app.BussinessLogic.api as api
from bson.json_util import dumps
app = Flask(__name__)

''' 
private function to convert MultiOrderedDict to dictionary, 
and converting the value from list to an object 
'''
def __to_dict(data):
    data = dict(data)
    for datum in data.keys():
        data[datum] = data[datum][0]
    return data

'''
test API to check connection to the web server
'''
@app.route("/")
def test_connection():
    return dumps({"connection":"success"})

'''
secure API to get an user authenticated, 
given the authentication token and the username 
authentication token = username + separator + timestamp encrypted by password
'''
@app.route("/auth/username/<auth_token>")
def authenticate(username, auth_token):
    return dumps(api.authenticate(username, auth_token))

'''
API to register a user, 
given username, name, birth date and encrypted password
the password is encrypted with server's public key
'''
@app.route("/register", methods=['POST'])
def register():
    data = __to_dict(request.form)
    return dumps(api.register(cookie, data))

'''
API to get the list of atmost limit number of transactions for a user,
starting from the offset
'''
@app.route("/transactions/all/<int:offset>/<int:limit>")
def get_transactions(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_transactions(cookie, offset, limit))

'''
API to add a new transaction record for a user
given date, type, category, dealer, paid_status
'''
@app.route("/transactions/add", methods=['POST'])
def add_transaction():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    data = __to_dict(request.form)
    return dumps(api.add_transactions(cookie, data))

'''
API to delete a transaction record for a user
given the id of the document
'''
@app.route("/transactions/delete/<doc_id>")
def delete_transaction(doc_id):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.delete_transactions(cookie, doc_id))

'''
API to get the transaction record for a user 
given the id of the document
'''
@app.route("/transactions/id/<doc_id>")
def get_transaction_by_id(doc_id):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_transaction_by_id(cookie, doc_id))

'''
API to update the transaction record for a user
given the previous transaction details
'''
@app.route("/transactions/edit", methods=['POST'])
def update_transactions():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    data = __to_dict(request.form)
    return dumps(api.update_transactions(cookie, data))

'''
API to get the list of atmost limit number of debts for a user,
starting from the offset
'''
@app.route("/debts/all/<int:offset>/<int:limit>")
def get_debt_list(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    data = __to_dict(request.form)
    return dumps(api.get_debt_list(cookie, offset, limit))

'''
API to update the paid_status of the debts for a user
given the transactions id list
'''
@app.route("/debts/update", methods=['POST'])
def update_debt_list():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    data = __to_dict(request.form)
    return dumps(api.update_debt_list(cookie, data))

'''
API to get the list of atmost limit number of owes for a user,
starting from the offset
'''
@app.route("/owes/all/<int:offset>/<int:limit>")
def get_owe_list(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_owe_list(cookie, offset, limit))

'''
API to update the paid_status of the owes for a user
given the transactions id list
'''
@app.route("/owes/update", methods=['POST'])
def update_owe_list():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    data = __to_dict(request.form)
    return dumps(api.update_owe_list(cookie, offset, limit))

'''
API to get the list of all categories of money spent for a user
'''
@app.route("/categories/all")
def get_all_categories():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_all_categories(cookie))

'''
API to get the summary data grouped by category, for a user
'''
@app.route("/summary/category")
def get_summary_by_category():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_summary_by_category(cookie))

'''
API to get the summary data grouped by weekdays, for a user
'''
@app.route("/summary/weekdays")
def get_summary_by_weekdays():
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_summary_by_weekdays(cookie))

'''
API to get list of atmost limit number of credit transactions for a user,
starting from the offset 
'''
@app.route("/transactions/category/credit/<int:offset>/<int:limit>")
def get_credit_transactions(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_credit_transactions(cookie, offset, limit))

'''
API to get list of atmost limit number of debit transactions for a user,
starting from the offset
'''
@app.route("/transactions/category/debit/<int:offset>/<int:limit>")
def get_debit_transactions(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_debit_transactions(cookie, offset, limit))

'''
API to get list of atmost limit number of save type transactions for a user,
starting from the offset
'''
@app.route("/transactions/category/save/<int:offset>/<int:limit>")
def get_saved_transactions(offset, limit):
    if "auth" not in request.headers.keys():
        return dumps({"authentication":"fail"})
    cookie = request.headers.get("auth")
    return dumps(api.get_saved_transactions(cookie, offset, limit))

'''
The default handler
'''
@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def pnf(path):
    return json.dumps({"status":404, "path":path})

'''
function called by the main program to start the web server
'''
def start_server():
    app.run(threaded = True)
    # app.run(processes = 10)