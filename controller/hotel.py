from flask import jsonify

from model.hotel import HotelDAO


class Hotel:

    def make_json(self, tuples):
        result = []
        for t in tuples:
            D = {}
            D['hid'] = t[0]
            D['chain'] = t[1]
            D['name'] = t[2]
            D['city'] = t[3]
            result.append(D)

        return result

    def make_json_one(self, hotel):
        result = {}
        result['hid'] = hotel[0]
        result['chain'] = hotel[1]
        result['name'] = hotel[2]
        result['city'] = hotel[3]

        return result

    def getAllHotels(self):
        model = HotelDAO()
        result = model.getAllHotels()
        answer = self.make_json(result)
        return answer

    def addNewHotel(self, data):
        chain = data['chain']
        name = data['name']
        city = data['city']
        dao = HotelDAO()
        hotel = dao.addNewHotel(chain, name, city)
        result = self.make_json(hotel)
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
            result = self.make_json_one(hotel)
            return result
