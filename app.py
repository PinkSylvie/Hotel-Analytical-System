from flask import Flask, request, jsonify
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
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"),404

            valid_keys = {'cname', 'springmkup', 'summermkup', 'fallmkup', 'wintermkup'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"),404
    
            handler = Chains()
            return handler.addNewChain(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"),404


@app.route("/chains/<int:chid>",methods=['GET', 'PUT', 'DELETE'])
def handleChainById(chid):
    if request.method == 'GET':
        handler = Chains()
        return handler.getChainById(chid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"),404

            valid_keys = {'cname', 'springmkup', 'summermkup', 'fallmkup', 'wintermkup'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"),404

            handler = Chains()
            return handler.updateChainById(chid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"),404
    else:
        try:
            handler = Chains()
            return handler.deleteChainById(chid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"),404


@app.route("/employee",methods=['GET', 'POST'])
def handleEmployee():
    if request.method == 'GET':
        handler = Employee()
        return handler.getAllEmployees()
    else:
        try:
            data = request.json
            if not data:
                return jsonify('No data provided'), 404

            valid_keys = {'hid', 'fname', 'lname', 'age', 'position', 'salary'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Employee()
            return handler.addNewEmployee(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404


@app.route("/employee/<int:eid>",methods=['GET', 'PUT', 'DELETE'])
def handleEmployeeById(eid):
    if request.method == 'GET':
        handler = Employee()
        return handler.getEmployeeById(eid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'hid', 'fname', 'lname', 'age', 'position', 'salary'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Employee()
            return handler.updateEmployeeById(eid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404

    else:
        try:
            handler = Employee()
            return handler.deleteEmployeeById(eid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"),404


@app.route("/hotel/<int:hid>/highestpaid", methods=['GET'])
def handleHighestPaid(hid):
    handler = Employee()
    return handler.getHighestPaid(hid)


@app.route("/most/revenue", methods=['GET'])
def handleTopRevenue():
    handler = Chains()
    return handler.getTopRevenue()


@app.route("/least/rooms", methods=['GET'])
def handleLeastRooms():
    handler = Chains()
    return handler.getLeastRooms()


if __name__ == "__main__":
    app.run(debug=True)

