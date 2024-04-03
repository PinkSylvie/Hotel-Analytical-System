from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.chains import Chains
from controller.employee import Employee
from controller.stats import Stats


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

# Local Stats
@app.route("/hotel/<int:hid>/highestpaid", methods=['GET'])
def handleHighestPaid(hid):
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckAccess(hid, eid)
        if access:
            return handler.getHighestPaid(hid)
        else:
            return jsonify("This employee has no access to these stats"), 404
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


# Global Stats
@app.route("/most/revenue", methods=['GET'])
def handleTopRevenue():
    handler = Stats()
    return handler.getTopRevenue()


@app.route("/least/rooms", methods=['GET'])
def handleLeastRooms():
    handler = Stats()
    return handler.getLeastRooms()


if __name__ == "__main__":
    app.run(debug=True)

