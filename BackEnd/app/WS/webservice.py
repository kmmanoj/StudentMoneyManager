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
missing_header_error = dumps({'status':200, 'error':'Missing header username', 'response':None})
method_not_allowed = dumps({'status':405, 'error': 'Method not allowed', 'response':None})
methods_list = ['GET','POST','PUT','DELETE','LOCK','HEAD','TRACE','PATCH','UNLOCK','OPTIONS','VIEW','PURGE','COPY','LINK','UNLINK','PROPFIND']

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
@app.route('/', methods = methods_list)
def test_connection():
    return dumps({'connection':'success'})

'''
secure API to get an user authenticated, 
given the authentication token and the username 
authentication token = username + separator + TS encrypted by password
'''
# @app.route('/auth/<auth_token>')
@app.route('/auth/<username>/<password>',methods = methods_list)
# def authenticate(username, auth_token):
def authenticate(username, password):
    if request.method == 'GET':
        return dumps(api.authenticate(username, password))
    else:
        return method_not_allowed

'''
API to register a user, 
given username, name, birth date and encrypted password
the password is encrypted with server's public key
'''
@app.route('/register', methods = methods_list)
def register():
    if request.method == 'POST':
        data = __to_dict(request.form)
        return dumps(api.register(data))
    else:
        return method_not_allowed

'''
API to check if a user with username already exists
'''
@app.route('/user/<username>', methods = methods_list)
def check_user(username):
    if request.method == 'GET':
        return dumps(api.check_user(username))
    else:
        return method_not_allowed

'''
API to get the list of atmost limit number of transactions for a user,
starting from the offset
'''
@app.route('/transactions/all/<int:offset>/<int:limit>', methods = methods_list)
def get_transactions(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_transactions(user, offset, limit))
    else:
        return method_not_allowed

'''
API to add a new transaction record for a user
given date, type, category, dealer, paid_status
'''
@app.route('/transactions/add', methods = methods_list)
def add_transaction():
    if request.method == 'POST':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        data = __to_dict(request.form)
        return dumps(api.add_transaction(user, data))
    else:
        return method_not_allowed

'''
API to delete a transaction record for a user
given the id of the document
'''
@app.route('/transactions/delete/<doc_id>', methods = methods_list)
def delete_transaction(doc_id):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.delete_transaction(user, doc_id))
    else:
        return method_not_allowed

'''
API to get the transaction record for a user 
given the id of the document
'''
@app.route('/transactions/id/<doc_id>', methods = methods_list)
def get_transaction_by_id(doc_id):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_transaction_by_id(user, doc_id))
    else:
        return method_not_allowed

'''
API to update the transaction record for a user
given the previous transaction details
'''
@app.route('/transactions/edit', methods = methods_list)
def update_transactions():
    if request.method == 'POST':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        data = __to_dict(request.form)
        return dumps(api.update_transactions(user, data))
    else:
        return method_not_allowed

'''
API to get the list of at most limit number of debts for a user,
starting from the offset
'''
@app.route('/debts/all/<int:offset>/<int:limit>', methods = methods_list)
def get_debt_list(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        data = __to_dict(request.form)
        return dumps(api.get_debt_list(user, offset, limit))
    else:
        return method_not_allowed

'''
API to update the paid_status of the debts for a user
given the transactions id list
'''
@app.route('/debts/update', methods = methods_list)
def update_debt_list():
    if request.method == 'POST':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        data = __to_dict(request.form)
        return dumps(api.update_debt_list(user, data))
    else:
        return method_not_allowed

'''
API to get the list of atmost limit number of owes for a user,
starting from the offset
'''
@app.route('/owes/all/<int:offset>/<int:limit>', methods = methods_list)
def get_owe_list(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_owe_list(user, offset, limit))
    else:
        return method_not_allowed

'''
API to update the paid_status of the owes for a user
given the transactions id list
'''
@app.route('/owes/update', methods = methods_list)
def update_owe_list():
    if request.method == 'POST':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        data = __to_dict(request.form)
        return dumps(api.update_owe_list(user, data))
    else:
        return method_not_allowed

'''
API to get the list of all categories of money spent for a user
'''
@app.route('/categories/all', methods = methods_list)
def get_all_categories():
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_all_categories(user))
    else:
        return method_not_allowed

'''
API to get the summary data grouped by category, for a user
'''
@app.route('/summary/category', methods = methods_list)
def get_summary_by_category():
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_summary_by_category(user))
    else:
        return method_not_allowed

'''
API to get the summary data grouped by weekdays, for a user
'''
@app.route('/summary/weekdays', methods = methods_list)
def get_summary_by_weekdays():
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_summary_by_weekdays(user))
    else:
        return method_not_allowed

'''
API to get list of atmost limit number of credit transactions for a user,
starting from the offset 
'''
@app.route('/transactions/type/credit/<int:offset>/<int:limit>', methods = methods_list)
def get_credit_transactions(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_credit_transactions(user, offset, limit))
    else:
        return method_not_allowed

'''
API to get list of atmost limit number of debit transactions for a user,
starting from the offset
'''
@app.route('/transactions/type/debit/<int:offset>/<int:limit>', methods = methods_list)
def get_debit_transactions(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_debit_transactions(user, offset, limit))
    else:
        return method_not_allowed

'''
API to get list of atmost limit number of save type transactions for a user,
starting from the offset
'''
@app.route('/transactions/type/save/<int:offset>/<int:limit>', methods = methods_list)
def get_saved_transactions(offset, limit):
    if request.method == 'GET':
        if 'User' not in request.headers.keys():
            return missing_header_error
        user = request.headers.get('User')
        return dumps(api.get_saved_transactions(user, offset, limit))
    else:
        return method_not_allowed

'''
The default handler
'''
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def pnf(path):
    return dumps({'status':404, 'path':path})

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