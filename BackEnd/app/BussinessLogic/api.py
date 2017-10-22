import app.ORM.orm as orm

def get_transactions(offset, limit):
    response = dict()
    response['data'] = orm.get_transactions(offset, limit)
    return response

def add_transaction(request):
    response = dict()
    response['status'] = orm.add_transaction(request)
    return response

def delete_transaction(timestamp):
    response = dict()
    response['status'] = orm.delete_transaction(timestamp)
    return response

def edit_transaction(timestamp, updated):
    response = dict()
    response['status'] = orm.edit_transaction(timestamp, updated)
    return response

def get_debt_list(offset, limit):
    response = dict()
    response['data'] = orm.get_debt_list(offset, limit)
    return response

def add_debt(request):
    response = dict()
    response['status'] = orm.add_debt(request)
    return response

def delete_debt(timestamp):
    response = dict()
    response['status'] = orm.delete_debt(timestamp)
    return response

def edit_debt(timestamp, updated):
    response = dict()
    response['status'] = orm.edit_debt(timestamp, updated)
    return response

def get_owe_list(offset, limit):
    response = dict()
    response['data'] = orm.get_debt_list(offset, limit)
    return response

def add_owe(request):
    response = dict()
    response['status'] = orm.add_owe(request)
    return response

def delete_debt(timestamp):
    response = dict()
    response['status'] = orm.delete_debt(timestamp)
    return response

def edit_debt(timestamp, updated):
    response = dict()
    response['status'] = orm.edit_debt(timestamp, updated)
    return response