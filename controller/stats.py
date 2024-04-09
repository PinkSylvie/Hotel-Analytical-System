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

    def make_cap_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['hname'] = t[1]
            D['hcity'] = t[2]
            D['total_cap'] = t[3]
            result.append(D)
        return result

    def make_res_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['hname'] = t[1]
            D['hcity'] = t[2]
            D['reservation_count'] = t[3]
            D['percentile_rank'] = t[4]
            result.append(D)
        return result

    def make_discount_json(self, tuples):
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

    def make_least_reserve_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['ruid'] = t[0]
            D['rid'] = t[1]
            D['startdate'] = t[2]
            D['enddate'] = t[3]
            D['days_unavailable'] = t[4]
            result.append(D)
        return result

    def make_credit_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['clid'] = t[0]
            D['fname'] = t[1]
            D['lname'] = t[2]
            D['reservation_count'] = t[3]
            result.append(D)
        return result
    
    def make_handicaproom_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['rdid'] = t[0]
            D['rname'] = t[1]
            D['rtype'] = t[2]
            D['capacity'] = t[3]
            D['ishandicap'] = t[4]
            D['handicap_room_name'] = t[5]
            D['reservation_count'] = t[6]
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

    def getTopHotelCap(self):
        dao = StatsDAO()
        hotel = dao.getTopHotelCap()
        result = self.make_cap_json(hotel)
        return result

    def getTopHotelRes(self):
        dao = StatsDAO()
        hotel = dao.getTopHotelRes()
        result = self.make_res_json(hotel)
        return result

    def getTopCreditClient(self, hid):
        dao = StatsDAO()
        client = dao.getTopCreditClient(hid)
        result = self.make_credit_json(client)
        return result

    def getTopClientDiscount(self, hid):
        dao = StatsDAO()
        client = dao.getTopClientDiscount(hid)
        result = self.make_discount_json(client)
        return result
    
    def getTopHandicapRoom(self, hid):
        dao = StatsDAO()
        hotel = dao.getMostReservedHandicap(hid)
        result = self.make_handicaproom_json(hotel)
        return result

    def getLeastReserve(self, hid):
        dao = StatsDAO()
        ru = dao.getLeastReserve(hid)
        if not ru:
            return jsonify("Not Found"), 404
        else:
            result = self.make_least_reserve_json(ru)
            return result
