'''
Abstract driver that communicates with mongo db to gets required data in dictionary format

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
from pymongo import MongoClient
from bson.objectid import ObjectId
import calendar
from datetime import datetime
host = 'localhost:27017'
db = MongoClient(host)['StudentMoneyManager']

'''
function to get the details of the user given the username
'''
def get_details(username):
    db_result = dict()
    result = list()
    if 'userDB' in db.collection_names():
        result = list(db.userDB.find({'username':username}))
    if len(result) == 0:
        db_result['name'] = None
        db_result['username'] = username
        db_result['password'] = None
        db_result['dob'] = None
        return db_result
    result = result[0]
    db_result['name'] = result['name']
    db_result['username'] = result['username']
    db_result['password'] = result['password']
    db_result['dob'] = result['dob']
    return db_result
    
'''
function to add an user given the details into the list of users using the software 
'''
def add_user(name, date_of_birth, username, password):
    if db['userDB'].insert({'name':name, 'dob':date_of_birth, 'username':username, 'password':password}):
        return True
    else:
        return False

'''
function to get the list of all transactions for a user
by skipping offset and limiting the number of records to limit
'''
def get_transactions(user, offset, limit):
    return list(db[user].find().skip(offset).limit(limit))

'''
function to add a transaction for a user 
given the transaction details 
'''
def add_transaction(user, date, transaction_type, category, dealer, paid_status, amount):
    status = db[user].insert({'date':date, 'type':transaction_type, 'category':category, 'dealer':dealer, 'paid_status':paid_status, 'amount':amount})
    if status: return True
    else: return False

'''
function to delete a transaction of a user given the document id
'''
def delete_transaction(user, doc_id): 
    status = dict(db[user].remove({'_id':ObjectId(doc_id)}))
    if status['n'] != 0: return True
    else: return False

'''
function to get the transaction details of a user given the document id
'''
def get_transaction_by_id(user, doc_id):
    db_result = list(db[user].find({'_id':ObjectId(doc_id)}))
    if len(db_result) == 0: return dict()
    else: return db_result[0]

'''
function to update the transaction for a user whose id is given 
with the new values as specified in the parameters
'''
def update_transaction(user, doc_id, date, transaction_type, category, dealer, paid_status, amount):
    db_result = dict(db[user].update({'_id':ObjectId(doc_id)}, {'date':date, 'type':transaction_type, 'category':category, 'dealer':dealer, 'paid_status':paid_status, 'amount':amount},upsert=True))
    if db_result['n'] != 0: return True
    else: return False

'''
function to get the list of credit transactions whose paid status is not paid for a user
'''
def get_debt_list(user, offset, limit): 
    db_result = list(db[user].find({'$and':[{'type':'debit'},{'paid_status':'false'}]}).skip(offset).limit(limit))
    return db_result

'''
function to update the paid status of a transaction given the document id for a user
'''
def update_debt(user, doc_id):
    record = get_transaction_by_id(user, doc_id)
    if 'paid_status' not in record.keys(): return False
    record['paid_status'] = 'true'
    del record['_id']
    status = dict(db[user].update({'_id':doc_id}, record, {'upsert':True}))
    if status : return True
    else: return False

'''
function to get the list of debit transactions whose paid status is not paid for a user
'''
def get_owe_list(user, offset, limit): 
    db_result = list(db[user].find({'$and': [{'type':'credit'},{'paid_status':'false'}]}).skip(offset).limit(limit))
    return db_result

'''
function to update the paid status of a transaction given the document id for a user
'''
def update_owe(user, doc_id):
    record = get_transaction_by_id(user, doc_id)
    if 'paid_status' not in record.keys(): return False
    record['paid_status'] = 'true'
    del record['_id']
    status = dict(db[user].update({'_id':doc_id}, record, {'upsert':True}))
    if status : return True
    else: return False

'''
function that gets the unique list of all categories of transactions for a user
'''
def get_all_categories(user): 
    db_result = list(db[user].distinct('category'))
    if "" in db_result:
        db_result.remove("")
    return db_result

'''
function to get the summary credit, debit and save transactions for a user grouped by category
'''
def get_summary_by_category(user, category):
    db_result=list(db[user].find({'category':category}))
    return db_result

'''
function to get the summary of credit, debit and save transactions for a user grouped by weekdays
'''
def get_summary_by_weekday(user, day):
    db_result=list()
    for r in db[user].find():
	d=datetime.strptime(r['date'], "%d-%m-%Y")
	if calendar.day_name[d.weekday()]==day:
	    db_result.append(r)
    return db_result


'''
function to get the list of transactions of a specific type for a user
starting from the offset and limiting the number of records to a limit
'''
def get_transactions_of_type(user, offset, limit, transaction_type): 
    db_result = list(db[user].find({'type':transaction_type}).skip(offset).limit(limit))
    return db_result
