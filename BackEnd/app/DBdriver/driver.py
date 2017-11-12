'''
Abstract driver that communicates with mongo db to gets required data in dictionary format

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
from pymongo import MongoClient
from bson.objectid import ObjectId
host = '192.168.254.101:27017'
db = MongoClient(host)['StudentMoneyManager']

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
    
def add_user(name, date_of_birth, username, password):
    if db['userDB'].insert({'name':name, 'dob':date_of_birth, 'username':username, 'password':password}):
        return True
    else:
        return False

def get_transactions(user, offset, limit):
    return list(db[user].find().skip(offset).limit(limit))

def add_transaction(user, date, transaction_type, category, dealer, paid_status, amount):
    status = db[user].insert({'date':date, 'type':transaction_type, 'category':category, 'dealer':dealer, 'paid_status':paid_status, 'amount':amount})
    if status: return True
    else: return False

def delete_transaction(user, doc_id): 
    status = dict(db[user].remove({'_id':ObjectId(doc_id)}))
    if status['n'] != 0: return True
    else: return False

def get_transaction_by_id(user, doc_id):
    db_result = list(db[user].find({'_id':ObjectId(doc_id)}))
    if len(db_result) == 0: return dict()
    else: return db_result[0]

def update_transaction(user, doc_id, date, transaction_type, category, dealer, paid_status, amount):
    db_result = dict(db[user].update({'_id':ObjectId(doc_id)}, {'date':date, 'type':transaction_type, 'category':category, 'dealer':dealer, 'paid_status':paid_status, 'amount':amount},{'upsert':True}))
    if db_result['n'] != 0: return True
    else: return False

def get_debt_list(user, offset, limit): 
    db_result = list(db[user].find({'$and':[{'type':'credit'},{'paid_status':False}]}).skip(offset).limit(limit))
    return db_result

def update_debt(user, doc_id):
    record = get_transaction_by_id(user, doc_id)
    if 'paid_status' not in record.keys(): return False
    record['paid_status'] = True
    del record['_id']
    status = dict(db[user].update({'_id':doc_id}, record, {'upsert':True}))
    if status : return True
    else: return False

def get_owe_list(user, offset, limit): 
    db_result = list(db[user].find({'$and': [{'type':'credit'},{'paid_status':False}]}).skip(offset).limit(limit))
    return db_result

def update_owe(user, doc_id):
    record = get_transaction_by_id(user, doc_id)
    if 'paid_status' not in record.keys(): return False
    record['paid_status'] = True
    del record['_id']
    status = dict(db[user].update({'_id':doc_id}, record, {'upsert':True}))
    if status : return True
    else: return False

def get_all_categories(user): 
    db_result = db[user].distinct('categories')
    return db_result

def get_summary_by_category(user, category): 
    pass

def get_summary_by_weekday(user, day): 
    pass

def get_transactions_of_type(user, offset, limit, transaction_type): 
    db_result = list(db[user].find({'type':transaction_type}).skip(offset).limit(limit))
    return db_result
