from flask import jsonify

from model.room import RoomDAO

class Room:

    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rid'] = t[0]
            D['hid'] = t[1]
            D['rdid'] = t[2]
            D['rprice'] = t[3]
            result.append(D)

        return result

    def make_json_one(self, room):
        result = {}
        result['rid'] = room[0]
        result['hid'] = room[1]
        result['rdid'] = room[2]
        result['rprice'] = room[3]

        return result

    def getAllRooms(self):
        model = RoomDAO()
        result = model.getAllRooms()
        answer = self.make_json(result)
        return answer

    def addNewRoom(self, data):
        hid = data['hid']
        rdid = data['rdid']
        rprice = data['rprice']
        dao = RoomDAO()
        room = dao.addNewRoom(hid, rdid, rprice)
        result = self.make_json(room)
        return result

    def getRoomById(self, rid):
        dao = RoomDAO()
        room = dao.getRoomById(rid)
        if not room:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(room)
            return result

    def updateRoomById(self, rid, data):
        dao = RoomDAO()
        room = dao.updateRoomById(rid, data)
        if not room:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(room)
            return result

    def deleteRoomById(self, rid):
        dao = RoomDAO()
        room = dao.deleteRoomById(rid)
        if not room:
            return jsonify("Not Found"), 404
        else:
            result = "Succesfully deleted room with id  " + str(rid) + "!"
            return result

