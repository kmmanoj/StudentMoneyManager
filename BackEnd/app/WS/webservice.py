'''
WEB SERVICE APIs

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
from flask import Flask, request, abort
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
authentication token = username + separator + TS encrypted by password
'''
# @app.route("/auth/<auth_token>")
@app.route("/auth/<username>/<password>")
# def authenticate(username, auth_token):
def authenticate(username, password):
    return dumps(api.authenticate(username, password))

'''
API to register a user, 
given username, name, birth date and encrypted password
the password is encrypted with server's public key
'''
@app.route("/register", methods=['POST'])
def register():
    data = __to_dict(request.form)
    return dumps(api.register(data))

'''
API to check if a user with username already exists
'''
@app.route("/user/<username>")
def check_user(username):
    return dumps(api.check_user(username))

'''
API to get the list of atmost limit number of transactions for a user,
starting from the offset
'''
@app.route("/transactions/all/<int:offset>/<int:limit>")
def get_transactions(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_transactions(user, offset, limit))

'''
API to add a new transaction record for a user
given date, type, category, dealer, paid_status
'''
@app.route("/transactions/add", methods=['POST'])
def add_transaction():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    data = __to_dict(request.form)
    return dumps(api.add_transactions(user, data))

'''
API to delete a transaction record for a user
given the id of the document
'''
@app.route("/transactions/delete/<doc_id>")
def delete_transaction(doc_id):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.delete_transactions(user, doc_id))

'''
API to get the transaction record for a user 
given the id of the document
'''
@app.route("/transactions/id/<doc_id>")
def get_transaction_by_id(doc_id):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_transaction_by_id(user, doc_id))

'''
API to update the transaction record for a user
given the previous transaction details
'''
@app.route("/transactions/edit", methods=['POST'])
def update_transactions():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    data = __to_dict(request.form)
    return dumps(api.update_transactions(user, data['ids']))

'''
API to get the list of atmost limit number of debts for a user,
starting from the offset
'''
@app.route("/debts/all/<int:offset>/<int:limit>")
def get_debt_list(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    data = __to_dict(request.form)
    return dumps(api.get_debt_list(user, offset, limit))

'''
API to update the paid_status of the debts for a user
given the transactions id list
'''
@app.route("/debts/update", methods=['POST'])
def update_debt_list():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    data = __to_dict(request.form)
    return dumps(api.update_debt_list(user, data))

'''
API to get the list of atmost limit number of owes for a user,
starting from the offset
'''
@app.route("/owes/all/<int:offset>/<int:limit>")
def get_owe_list(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_owe_list(user, offset, limit))

'''
API to update the paid_status of the owes for a user
given the transactions id list
'''
@app.route("/owes/update", methods=['POST'])
def update_owe_list():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    data = __to_dict(request.form)
    return dumps(api.update_owe_list(user, offset, limit))

'''
API to get the list of all categories of money spent for a user
'''
@app.route("/categories/all")
def get_all_categories():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_all_categories(user))

'''
API to get the summary data grouped by category, for a user
'''
@app.route("/summary/category")
def get_summary_by_category():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_summary_by_category(user))

'''
API to get the summary data grouped by weekdays, for a user
'''
@app.route("/summary/weekdays")
def get_summary_by_weekdays():
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_summary_by_weekdays(user))

'''
API to get list of atmost limit number of credit transactions for a user,
starting from the offset 
'''
@app.route("/transactions/category/credit/<int:offset>/<int:limit>")
def get_credit_transactions(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_credit_transactions(user, offset, limit))

'''
API to get list of atmost limit number of debit transactions for a user,
starting from the offset
'''
@app.route("/transactions/category/debit/<int:offset>/<int:limit>")
def get_debit_transactions(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_debit_transactions(user, offset, limit))

'''
API to get list of atmost limit number of save type transactions for a user,
starting from the offset
'''
@app.route("/transactions/category/save/<int:offset>/<int:limit>")
def get_saved_transactions(offset, limit):
    if "user" not in request.headers.keys():
        return dumps({"error":"missing header user"})
    user = request.headers.get("user")
    return dumps(api.get_saved_transactions(user, offset, limit))

'''
The default handler
'''
@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def pnf(path):
    return dumps({"status":404, "path":path})

'''
The authorization gateway
'''
@app.before_request
def trusted_web_app_servers():
    if request.remote_addr != '127.0.0.1':
        abort(403)

'''
function called by the main program to start the web server
'''
def start_server():
    app.run(threaded = True)
    # app.run(processes = 10)