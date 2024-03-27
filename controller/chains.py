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

    def getChainById(self,chid):
        dao = ChainsDAO()
        chain = dao.getChainById(chid)
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
            result = self.make_json_one(chain)
            return result
