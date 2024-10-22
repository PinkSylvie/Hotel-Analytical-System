from flask import jsonify

from model.reserve import ReserveDAO
class Reserve:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['reid'] = t[0]
            D['ruid'] = t[1]
            D['clid'] = t[2]
            D['total_cost'] = t[3]
            D['payment'] = t[4]
            D['guests'] = t[5]
            result.append(D)

        return result

    def make_json_one(self, reserve):
        result = {}
        result['reid'] = reserve[0]
        result['ruid'] = reserve[1]
        result['clid'] = reserve[2]
        result['total_cost'] = reserve[3]
        result['payment'] = reserve[4]
        result['guests'] = reserve[5]

        return result

    def getAllReserve(self):
        model = ReserveDAO()
        result = model.getAllReserve()
        answer = self.make_json(result)
        return answer

    def addNewReserve(self, data):
        ruid = data['ruid']
        clid = data['clid']
        payment = data['payment']
        guests = data['guests']
        dao = ReserveDAO()
        reserve = dao.addNewReserve(ruid,clid,payment,guests)
        if not reserve:
            return jsonify("Room is reserved by someone else"), 404
        else:
            result = self.make_json_one(reserve)
            return result

    def getReserveById(self, reid):
        dao = ReserveDAO()
        reserve = dao.getReserveById(reid)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(reserve)
            return result

    def updateReserveById(self, reid, data):
        dao = ReserveDAO()
        reserve = dao.updateReserveById(reid, data)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(reserve)
            return result

    def deleteReserveById(self, reid):
        dao = ReserveDAO()
        reserve = dao.deleteReserveById(reid)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = "Succesfully deleted reservation with ID  " + str(reid) + "!"
            return result
