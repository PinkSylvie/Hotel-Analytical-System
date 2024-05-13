from flask import jsonify

from model.client import ClientDAO


class Client:

    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['clid'] = t[0]
            D['fname'] = t[1]
            D['lname'] = t[2]
            D['age'] = t[3]
            D['memberyear'] = t[4]
            result.append(D)

        return result

    def make_json_one(self, client):
        result = {}
        result['clid'] = client[0]
        result['fname'] = client[1]
        result['lname'] = client[2]
        result['age'] = client[3]
        result['memberyear'] = client[4]

        return result

    def getAllClients(self):
        model = ClientDAO()
        result = model.getAllClients()
        answer = self.make_json(result)
        return answer

    def addNewClient(self, data):
        fname = data['fname']
        lname = data['lname']
        age = data['age']
        memberyear = data['memberyear']
        dao = ClientDAO()
        client = dao.addNewClient(fname, lname, age, memberyear)
        result = self.make_json(client)
        return result

    def getClientById(self, clid):
        dao = ClientDAO()
        client = dao.getClientById(clid)
        if not client:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(client)
            return result

    def updateClientById(self, clid, data):
        dao = ClientDAO()
        client = dao.updateClientById(clid, data)
        if not client:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(client)
            return result

    def deleteClientById(self, clid):
        dao = ClientDAO()
        client = dao.deleteClientById(clid)
        if not client:
            return jsonify("Not Found"), 404
        else:
            result = "Succesfully deleted client with id " + str(clid) + "!"
            return result


