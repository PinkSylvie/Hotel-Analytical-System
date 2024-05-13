from flask import jsonify

from model.roomdescription import RoomdescriptionDAO
class Roomdescription:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rdid'] = t[0]
            D['rname'] = t[1]
            D['rtype'] = t[2]
            D['capacity'] = t[3]
            D['ishandicap'] = t[4]
            result.append(D)

        return result

    def make_json_one(self,roomdescription):
        result = {}
        result['rdid'] = roomdescription[0]
        result['rname'] = roomdescription[1]
        result['rtype'] = roomdescription[2]
        result['capacity'] = roomdescription[3]
        result['ishandicap'] = roomdescription[4]

        return result

    def getAllRoomdescriptions(self):
        model = RoomdescriptionDAO()
        result = model.getAllRoomdescriptions()
        answer = self.make_json(result)
        return answer

    def addRoomDescription(self, data):
        rname = data['rname']
        rtype = data['rtype']
        capacity = data['capacity']
        ishandicap = data['ishandicap']

        dao = RoomdescriptionDAO()
        ru = dao.addRoomdescription(rname, rtype, capacity, ishandicap)
        result = self.make_json_one(ru)
        return result
    
    def updateRoomDescriptionById(self, rdid, data):
        dao = RoomdescriptionDAO()
        ru = dao.updateRoomdescriptionById(rdid, data)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(ru)
            return result

    def getRoomdescriptionById(self,rdid):
        dao = RoomdescriptionDAO()
        room = dao.getRoomdescriptionById(rdid)
        if not room:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(room)
            return result

    def deleteRoomdescriptionById(self,rdid):
        dao = RoomdescriptionDAO()
        room = dao.deleteRoomdescriptionById(rdid)
        if not room:
            return jsonify("Not Found"), 404
        else:
            result = "Successfully deleted room description with ID " + str(room) + "!"
            return result