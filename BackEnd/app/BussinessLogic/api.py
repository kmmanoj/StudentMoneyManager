'''
BUSSINESS LOGIC, that handles complex functionalities

Author: Manoj Vignesh K M
version : 1.0.0
Date : 8 November 2017
'''
import app.DBdriver.driver as driver

def authenticate(username, auth_token): pass
def register(cookie, data): pass
def get_transactions(cookie, offset, limit): pass
def add_transaction(cookie, data): pass
def delete_transaction(cookie, doc_id): pass
def get_transaction_by_id(cookie, doc_id): pass
def update_transactions(cookie, data): pass
def get_debt_list(cookie, offset, limit): pass
def update_debt_list(cookie, data): pass
def get_owe_list(cookie, offset, limit): pass
def update_owe_list(cookie, offset, limit): pass
def get_all_categories(cookie): pass
def get_summary_by_category(cookie): pass
def get_summary_by_weekdays(cookie): pass
def get_credit_transactions(cookie, offset, limit): pass
def get_debit_transactions(cookie, offset, limit): pass
def get_saved_transactions(cookie, offset, limit): pass