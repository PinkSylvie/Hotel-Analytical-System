from flask import jsonify

from model.hotel import HotelDAO


class Hotel:

    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['chid'] = t[1]
            D['hname'] = t[2]
            D['hcity'] = t[3]
            result.append(D)

        return result

    def make_json_one(self, hotel):
        result = {}
        result['hid'] = hotel[0]
        result['chid'] = hotel[1]
        result['hname'] = hotel[2]
        result['hcity'] = hotel[3]

        return result

    def getAllHotels(self):
        model = HotelDAO()
        result = model.getAllHotels()
        answer = self.make_json(result)
        return answer

    def addNewHotel(self, data):
        chid = data['chid']
        hname = data['hname']
        hcity = data['hcity']
        dao = HotelDAO()
        hotel = dao.addNewHotel(chid, hname, hcity)
        result = self.make_json_one(hotel)
        return result

    def getHotelById(self, hid):
        dao = HotelDAO()
        hotel = dao.getHotelById(hid)
        if not hotel:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(hotel)
            return result

    def updateHotelById(self, hid, data):
        dao = HotelDAO()
        hotel = dao.updateHotelById(hid, data)
        if not hotel:
            return jsonify("Not Found"), 404
        else:
            result = self.make_json_one(hotel)
            return result

    def deleteHotelById(self, hid):
        dao = HotelDAO()
        hotel = dao.deleteHotelById(hid)
        if not hotel:
            return jsonify("Not Found"), 404
        else:
            result = "Succesfully deleted hotel with id " + str(hid) + "!"
            return result

