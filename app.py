from flask import Flask, request, jsonify
from flask_cors import CORS
from controller.chains import Chains
from controller.employee import Employee
from controller.hotel import Hotel
from controller.client import Client
from controller.stats import Stats
from controller.roomunavailable import RoomUnavailable
from controller import login, roomdescription
from controller.room import Room

app = Flask(__name__)
CORS(app)


@app.route("/")
def hello_world():
    return "Hello World my friends"

@app.route("/climp/login", methods=['POST'])
def handleLogin():
    if request.method == 'POST':
        handler = login.Login()

# Chains-----------------------------------------------------------------------------------------------------------
@app.route("/climp/chains", methods=['GET', 'POST'])
def handleChains():
    if request.method == 'GET':
        handler = Chains()
        return handler.getAllChains()
    else:
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'cname', 'springmkup', 'summermkup', 'fallmkup', 'wintermkup'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Chains()
            return handler.addNewChain(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/chains/<int:chid>", methods=['GET', 'PUT', 'DELETE'])
def handleChainById(chid):
    if request.method == 'GET':
        handler = Chains()
        return handler.getChainById(chid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'cname', 'springmkup', 'summermkup', 'fallmkup', 'wintermkup'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Chains()
            return handler.updateChainById(chid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"), 404
    else:
        try:
            handler = Chains()
            return handler.deleteChainById(chid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 200

# Employee-----------------------------------------------------------------------------------------------------------
@app.route("/climp/employee", methods=['GET', 'POST'])
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


@app.route("/climp/employee/<int:eid>", methods=['GET', 'PUT', 'DELETE'])
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
            return jsonify("Can not delete record because it is referenced by other records"), 404


# Hotel-----------------------------------------------------------------------------------------------------------
@app.route("/climp/hotel", methods=['GET', 'POST'])
def handleHotels():
    if request.method == 'GET':
        handler = Hotel()
        return handler.getAllHotels()
    else:
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'chid', 'hname', 'hcity'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Hotel()
            return handler.addNewHotel(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/hotel/<int:hid>", methods=['GET', 'PUT', 'DELETE'])
def handleHotelById(hid):
    if request.method == 'GET':
        handler = Hotel()
        return handler.getHotelById(hid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'chid', 'hname', 'hcity'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Hotel()
            return handler.updateHotelById(hid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"), 404
    else:
        try:
            handler = Hotel()
            return handler.deleteHotelById(hid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 404


# Client-----------------------------------------------------------------------------------------------------------

@app.route("/climp/client", methods=['GET', 'POST'])
def handleClients():
    if request.method == 'GET':
        handler = Client()
        return handler.getAllClients()
    else:
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'fname', 'lname', 'age', 'memberyear'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Client()
            return handler.addNewClient(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/client/<int:clid>", methods=['GET', 'PUT', 'DELETE'])
def handleClientById(clid):
    if request.method == 'GET':
        handler = Client()
        return handler.getClientById(clid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'fname', 'lname', 'age', 'memberyear'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Client()
            return handler.updateClientById(clid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"), 404
    else:
        try:
            handler = Client()
            return handler.deleteClientById(clid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 404

# Room Unavailable-----------------------------------------------------------------------------------------------------------

@app.route('/climp/roomunavailable', methods=['GET', 'POST'])
def handleRoomUnavailable():
    if request.method == 'GET':
        handler = RoomUnavailable()
        return handler.getAllRoomUnavailable()
    else:
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"),404

            valid_keys = {'rid', 'startdate', 'enddate'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"),404

            handler = RoomUnavailable()
            return handler.addNewRoomUnavailable(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"),404

@app.route('/climp/roomunavailable/<int:ruid>', methods=['GET','PUT','DELETE'])
def handleRoomUnavailableByRuid(ruid):
    if request.method == 'GET':
        handler = RoomUnavailable()
        return handler.getRoomUnavailableByRuid(ruid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"),404

            valid_keys = {'rid', 'startdate', 'enddate'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"),404

            handler = RoomUnavailable()
            return handler.updateRoomUnavailableByRuid(ruid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"),404
    else:
        try:
            handler = RoomUnavailable()
            return handler.deleteRoomUnavailableByRuid(ruid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"),200

# Room-----------------------------------------------------------------------------------------------------------
@app.route("/climp/room", methods=['GET', 'POST'])
def handleRoom():
    if request.method == 'GET':
        handler = Room()
        return handler.getAllRooms()
    else:
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'hid', 'rdid', 'rprice'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Room()
            return handler.addNewRoom(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/room/<int:rid>", methods=['GET', 'PUT', 'DELETE'])
def handleRoomById(rid):
    if request.method == 'GET':
        handler = Room()
        return handler.getRoomById(rid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404

            valid_keys = {'hid', 'rdid', 'rprice'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 404

            handler = Room()
            return handler.updateRoomById(rid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"), 404
    else:
        try:
            handler = Room()
            return handler.deleteRoomById(rid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 404

# Room Description-----------------------------------------------------------------------------------------------------------
@app.route("/climp/roomdescription", methods=['GET', 'POST'])
def handleRoomDescription():
    if request.method == 'GET':
        handler = roomdescription.Roomdescription()
        return handler.getAllRoomdescriptions()
    elif request.method == 'POST':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404
            
            valid_keys = {'rname', 'rtype', 'capacity', 'ishandicap'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 

            handler = roomdescription.Roomdescription()
            return handler.addRoomDescription(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404

@app.route("/climp/roomdescription/<int:rid>", methods=['GET', 'PUT', 'DELETE'])
def handleRoomDescriptionById(rid):
    if request.method == 'GET':
        handler = roomdescription.Roomdescription()
        return handler.getRoomdescriptionById(rid)
    elif request.method == 'PUT':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404
            
            valid_keys = {'rname', 'rtype', 'capacity', 'ishandicap'}
            if not all(key in data for key in valid_keys):
                    return jsonify("Missing a key"), 404
            
            handler = roomdescription.Roomdescription()
            return handler.updateRoomDescriptionById(rid, data)
    
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid data provided"), 404
    elif request.method == 'DELETE':
        try:
            handler = roomdescription.Roomdescription()
            return handler.deleteRoomdescriptionById(lid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 404
        
# Log In-----------------------------------------------------------------------------------------------------------
@app.route("/climp/login", methods=['GET', 'POST'])
def handleLogIn():
    if request.method == 'GET':
        handler = login.Login()
        return handler.getAllLogins()
    elif request.method == 'POST':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404
            
            valid_keys = {'eid', 'username', 'password'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 

            handler = login.Login()
            return handler.addLogIn(data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404
        
@app.route("/climp/login/<int:rid>", methods=['GET', 'POST'])
def handleLogInById(lid):
    if request.method == 'GET':
        handler = login.Login()
        return handler.getLoginById()
    elif request.method == 'POST':
        try:
            data = request.json
            if not data:
                return jsonify("No data provided"), 404
            
            valid_keys = {'eid', 'username', 'password'}
            if not all(key in data for key in valid_keys):
                return jsonify("Missing a key"), 

            handler = login.Login()
            return handler.updateLogInById(lid, data)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Invalid JSON data provided"), 404
    elif request.method == 'DELETE':
        try:
            handler = login.Login()
            return handler.deleteLogInById(lid)
        except Exception as e:
            print("Error processing request:", e)
            return jsonify("Can not delete record because it is referenced by other records"), 404



# Reserve-----------------------------------------------------------------------------------------------------------

# Local Stats
@app.route("/climp/hotel/<int:hid>/highestpaid", methods=['GET'])
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
        access = handler.CheckLocalAccess(hid, eid)
        if access:
            return handler.getHighestPaid(hid)
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/hotel/<int:hid>/mostdiscount", methods=['GET'])
def handleTopDiscounts(hid):
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckLocalAccess(hid, eid)
        if access:
            return handler.getTopClientDiscount(hid)
        else:
            return jsonify("This employee has no access to these stats"), 404
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/hotel/<int:hid>/mostcreditcard", methods=['GET'])
def handleTopCredit(hid):
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckLocalAccess(hid, eid)
        if access:
            return handler.getTopCreditClient(hid)
        else:
            return jsonify("This employee has no access to these stats"), 404
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404

@app.route('/climp/hotel/<int:hid>/leastreserve', methods=['GET'])
def handleLeastReserve(hid):
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404
        
        valid_key = {'eid'}
        if not all(key in data for key in valid_key):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckLocalAccess(hid, eid)
        if access:
            return handler.getLeastReserve(hid)
        else:
            return jsonify("This employee cannot access this statistic"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


# Global Stats
@app.route("/climp/most/revenue", methods=['GET'])
def handleTopRevenue():
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckGlobalAccess(eid)
        if access:
            return handler.getTopRevenue()
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/least/rooms", methods=['GET'])
def handleLeastRooms():
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckGlobalAccess(eid)
        if access:
            return handler.getLeastRooms()
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/most/capacity", methods=['GET'])
def handleTopHotelCap():
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckGlobalAccess(eid)
        if access:
            return handler.getTopHotelCap()
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


@app.route("/climp/most/reservation", methods=['GET'])
def handleTopHotelRes():
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404

        valid_keys = {'eid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckGlobalAccess(eid)
        if access:
            return handler.getTopHotelRes()
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404
    
@app.route("/climp/hotel/<int:hid>/handicaproom", methods=['GET'])
def handleTopHandicap(hid):
    try:
        data = request.json
        if not data:
            return jsonify("No data provided"), 404
        valid_keys = {'hid'}
        if not all(key in data for key in valid_keys):
            return jsonify("Missing a key"), 404
        eid = data['eid']
        handler = Stats()
        access = handler.CheckLocalAccess(hid, eid)
        if access:
            return handler.getTopHandicapRoom(hid)
        else:
            return jsonify("This employee has no access to these stats"), 200
    except Exception as e:
        print("Error processing request:", e)
        return jsonify("Invalid JSON data provided"), 404


if __name__ == "__main__":
    app.run(debug=True)
