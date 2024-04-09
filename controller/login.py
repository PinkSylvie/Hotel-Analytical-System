from flask import jsonify

from model.login import LoginDAO
class Login:
    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['lid'] = t[0]
            D['eid'] = t[1]
            D['username'] = t[2]
            D['password'] = t[3]
            result.append(D)

        return result

    def make_json_one(self,login):
        result = {}
        result['lid'] = login[0]
        result['eid'] = login[1]
        result['username'] = login[2]
        result['password'] = login[3]

        return result
    
    def getAllLogins(self):
        model = LoginDAO()
        result = model.getAllLogins()
        answer = self.make_json(result)
        return answer

    def getLoginById(self,lid):
        dao = LoginDAO()
        login = dao.getLoginById(lid)
        if not login:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(login)
            return result
        
    def addLogIn(self, data):
        lid = data['lid']
        eid = data['eid']
        username = data['username']
        password = data['password']
        dao = LoginDAO()
        login = dao.addNewLogin(lid, eid, username, password)
        result = self.make_json(login)
        return result
    
    def updateLogInById(self, lid, data):
        dao = LoginDAO()
        login = dao.updateLoginById(lid, data)
        
        if not login:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json(login)
            return result
        
    def deleteLogInById(self, lid):
        dao = LoginDAO()
        login = dao.deleteLoginById(lid)
        if not login:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json(login)
            return result
