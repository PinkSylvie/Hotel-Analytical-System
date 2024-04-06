from flask import jsonify

from model.stats import StatsDAO
class Stats:

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

    def make_highest_paid_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['eid'] = t[0]
            D['hid'] = t[1]
            D['fname'] = t[2]
            D['lname'] = t[3]
            D['age'] = t[4]
            D['position'] = t[5]
            D['salary'] = t[6]
            result.append(D)

        return result

    def CheckGlobalAccess(self, eid):
        dao = StatsDAO()
        access = dao.CheckGlobalAccess(eid)
        return access

    def CheckLocalAccess(self, hid, eid):
        dao = StatsDAO()
        access = dao.CheckLocalAccess(hid, eid)
        return access

    def getTopRevenue(self):
        dao = StatsDAO()
        chain = dao.getTopRevenue()
        result = self.make_revenue_json(chain)
        return result

    def getLeastRooms(self):
        dao = StatsDAO()
        chain = dao.getLeastRooms()
        result = self.make_least_room_json(chain)
        return result

    def getHighestPaid(self, hid):
        dao = StatsDAO()
        employee = dao.getHighestPaid(hid)
        if not employee:
            return jsonify("Not Found"), 404
        else:
            result = self.make_highest_paid_json(employee)
            return result
