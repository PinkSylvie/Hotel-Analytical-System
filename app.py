from flask import Flask, request
from flask_cors import CORS
from controller.chains import Chains
from controller.employee import Employee


app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "Hello World my friends"

@app.route("/chains", methods=['GET', 'POST'])
def handleChains():
    if request.method == 'GET':
        handler = Chains()
        return handler.getAllChains()
    else:
        return "Add Chain"

@app.route("/chains/<int:chid>",methods=['GET', 'PUT', 'DELETE'])
def handleChainById(chid):
    if request.method == 'GET':
        handler = Chains()
        return handler.getChainById(chid)
    elif request.method == 'PUT':
        #Still a WIP
        return "Update Chain"
    else:
        handler = Chains()
        #Still a WIP - Don't try - it explodes
        return handler.deleteChainById(chid)

@app.route("/employee",methods=['GET', 'POST'])
def handleEmployee():
    if request.method == 'GET':
        handler = Employee()
        return handler.getAllEmployees()
    else:
        # Still a WIP
        return "Add Employee"

@app.route("/employee/<int:eid>",methods=['GET', 'PUT', 'DELETE'])
def handleEmployeeById(eid):
    if request.method == 'GET':
        handler = Employee()
        return handler.getEmployeeById(eid)
    elif request.method == 'PUT':
        #Still a WIP
        return "Update Employee"
    else:
        #Still a WIP - Don't try - it explodes
        return "Delete Employee"


if __name__ == "__main__":
    app.run(debug=True)

