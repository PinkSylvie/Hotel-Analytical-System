from flask import jsonify

from model.chains import ChainsDAO
class Chains:


    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['cname'] = t[1]
            D['springmkup'] = t[2]
            D['summermkup'] = t[3]
            D['fallmkup'] = t[4]
            D['wintermkup'] = t[5]
            result.append(D)

        return result

    def make_revenue_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['cname'] = t[1]
            D['revenue'] = t[2]
            result.append(D)
        return result

    def make_least_room_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['chid'] = t[0]
            D['cname'] = t[1]
            D['room_amount'] = t[2]
            result.append(D)
        return result

    def make_json_one(self,chain):
        result = {}
        result['chid'] = chain[0]
        result['cname'] = chain[1]
        result['springmkup'] = chain[2]
        result['summermkup'] = chain[3]
        result['fallmkup'] = chain[4]
        result['wintermkup'] = chain[5]

        return result

    def getAllChains(self):
        model = ChainsDAO()
        result = model.getAllChains()
        answer = self.make_json(result)
        return answer

    def addNewChain(self, data):
        cname = data['cname']
        springmkup = data['springmkup']
        summermkup = data['summermkup']
        fallmkup = data['fallmkup']
        wintermkup = data['wintermkup']
        dao = ChainsDAO()
        chain = dao.addNewChain(cname,springmkup,summermkup,fallmkup,wintermkup)
        result = self.make_json(chain)
        return result

    def getChainById(self,chid):
        dao = ChainsDAO()
        chain = dao.getChainById(chid)
        if not chain:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(chain)
            return result

    def updateChainById(self, chid, data):
        dao = ChainsDAO()
        chain = dao.updateChainById(chid, data)
        if not chain:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(chain)
            return result

    def deleteChainById(self,chid):
        dao = ChainsDAO()
        chain = dao.deleteChainById(chid)
        if not chain:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json(chain)
            return result

    def getTopRevenue(self):
        dao = ChainsDAO()
        chain = dao.getTopRevenue()
        result = self.make_revenue_json(chain)
        return result

    def getLeastRooms(self):
        dao = ChainsDAO()
        chain = dao.getLeastRooms()
        result = self.make_least_room_json(chain)
        return result