from model.roomunavailable import RoomUnavailableDAO
from flask import jsonify

class RoomUnavailable:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['ruid'] = t[0]
            D['rid'] = t[1]
            D['startdate'] = t[2]
            D['enddate'] = t[3]
            result.append(D)
        return result
    
    def make_json_one(self, tuple):
        print("printing tuple", tuple)
        D = {}
        D['ruid'] = tuple[0]
        D['rid'] = tuple[1]
        D['startdate'] = tuple[2]
        D['enddate'] = tuple[3]
        return D
    
    def getAllRoomUnavailable(self):
        model = RoomUnavailableDAO()
        result = model.getAllRoomUnavailable()
        answer = self.make_json(result)
        return answer
    
    def addNewRoomUnavailable(self, data):
        rid = data['rid']
        startdate = data['startdate']
        enddate = data['enddate']
        dao = RoomUnavailableDAO()
        ru = dao.addNewRoomUnavailable(rid, startdate, enddate)
        result = self.make_json_one(ru)
        return result 
    
    def getRoomUnavailableByRuid(self, ruid):
        dao = RoomUnavailableDAO()
        ru = dao.getRoomUnavailableByRuid(ruid)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(ru)
            return result
    
    def updateRoomUnavailableByRuid(self, ruid, data):
        dao = RoomUnavailableDAO()
        ru = dao.updateRoomUnavailableByRuid(ruid, data)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(ru)
            return result
        
    def deleteRoomUnavailableByRuid(self, ruid):
        dao = RoomUnavailableDAO()
        ru = dao.deleteRoomUnavailableByRuid(ruid)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = "Succesfully deleted room unavailable with id " + str(ruid) + "!"
            return result
        
    def getByRid(self, rid):
        dao = RoomUnavailableDAO()
        ru = dao.getByRid(rid)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(ru)
            return result
    
    
    