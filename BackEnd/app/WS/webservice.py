from flask import Flask
import app.BussinessLogic.api as api
import json
app = Flask(__name__)

@app.route("/")
def test_connection():
    return json.dumps({"connection":"success"})

@app.route("/transactions/<int:offset>/<int:limit>")
def get_transactions(offset, limit):
    return json.dumps(api.get_transactions(offset, limit))

@app.route("/transactions/add", methods=['POST'])
def add_transaction():
    return json.dumps(api.add_transaction(request.form))

@app.route("/transactions/delete/<timestamp>")
def delete_transaction(timestamp):
    return json.dumps(api.delete_transaction(timestamp))

@app.route("/transactions/edit/<timestamp>", methods=['POST'])
def edit_transaction(timestamp):
    return json.dumps(api.edit_transaction(timestamp, request.form))

@app.route("/debt/<int:offset>/<int:limit>")
def get_debt_list(offset, limit):
    return json.dumps(api.get_debt_list(offset, limit))

@app.route("/debt/add", methods=['POST'])
def add_debt():
    return json.dumps(api.add_debt(request.form))

@app.route("/debt/delete/<timestamp>")
def delete_debt(timestamp):
    return json.dumps(api.delete_debt(timestamp))

@app.route("/debt/edit/<timestamp>")
def edit_debt(timestamp):
    return json.dumps(api.edit_debt(timestamp, request.form))

@app.route("/owe/<int:offset>/<int:limit>")
def get_owe_list(offset, limit):
    return json.dumps(api.get_owe_list(offset, limit))

@app.route("/owe/add", methods=['POST'])
def add_owe():
    return json.dumps(api.add_owe(request.form))

@app.route("/owe/delete/<timestamp>")
def delete_owe():
    return json.dumps(api.delete_owe(timestamp))

@app.route("/owe/edit/<timestamp>")
def edit_owe():
    return json.dumps(api.edit_owe(timestamp, request.form))

@app.route('/', defaults={'path': ''})
@app.route("/<path:path>")
def pnf(path):
    return json.dumps({"status":404, "path":path})

def start_server():
    app.run(threaded = True)
    # app.run(processes = 10)