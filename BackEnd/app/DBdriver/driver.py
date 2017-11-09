'''
Abstract driver that communicates with mongo db to gets required data in dictionary format

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
from pymongo import MongoClient
from bson.objectid import ObjectId
host = "192.168.254.101:27017"
db = MongoClient(host)['StudentMoneyManager']

def get_details(username):
    db_result = dict()
    result = list()
    if 'userDB' in db.collection_names():
        result = list(db.userDB.find({"username":username}))
    if len(result) == 0:
        db_result['name'] = None
        db_result['username'] = username
        db_result['password'] = None
        return db_result
    result = result[0]
    db_result['name'] = result['name']
    db_result['username'] = result['username']
    db_result['password'] = result['password']
    return db_result
    
def add_user(name, date_of_birth, username, password): pass
def get_transactions(user, offset, limit): pass
def add_transaction(user, date, type, category, dealer, status): pass 
def delete_transaction(user, doc_id): pass 
def get_transaction_by_id(user, doc_id): pass
def update_transactions(user, doc_id, date, type, category, dealer, status): pass
def get_debt_list(user, offset, limit): pass
def update_debt(user, doc_id): pass
def get_owe_list(user, offset, limit): pass
def update_owe_list(user, offset, limit): pass
def get_all_categories(user): pass
def get_summary_by_category(user): pass
def get_summary_by_weekdays(user): pass
def get_credit_transactions(user, offset, limit): pass
def get_debit_transactions(user, offset, limit): pass
def get_saved_transactions(user, offset, limit): pass