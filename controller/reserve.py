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
        total_cost = data['total_cost']
        payment = data['payment']
        guests = data['guests']
        dao = ReserveDAO()
        chain = dao.addNewReserve(ruid,clid,total_cost,payment,guests)
        result = self.make_json(chain)
        return result

    def getReserveById(self,eid):
        dao = ReserveDAO()
        reserve = dao.getReserveById(eid)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(reserve)
            return result

    def updateResrveById(self, reid, data):
        dao = ReserveDAO()
        reserve = dao.updateReserveById(reid, data)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(reserve)
            return result

    def deleteReserveById(self,eid):
        dao = ReserveDAO()
        reserve = dao.deleteReserveById(eid)
        if not reserve:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json(reserve)
            return result