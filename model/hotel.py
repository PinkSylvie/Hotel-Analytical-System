from config.dbconfig import pg_config
import psycopg2


class HotelDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllHotels(self):
        cursor = self.conn.cursor()
        query = "select hid, chain, name, city from hotel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getHotelById(self, hid):
        cursor = self.conn.cursor()
        query = "select hid, chain, name, city where hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewHotel(self, chain, name, city):

        cursor = self.conn.cursor()
        query = "insert into hotel (chain, name, city) values (%s, %s, %s);"
        cursor.execute(query, (chain, name, city))
        self.conn.commit()
        cursor.execute("SELECT * FROM hotel")
        result = cursor.fetchall()
        cursor.close()
        return result

    def updateHotelById(self, hid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update hotel set"

            if key == "chain":
                query += " chain = %s where hid = %s;"
            elif key == "name":
                query += " name = %s where hid = %s;"
            else:
                query += " city = %s where hid = %s;"
            cursor.execute(query, (value, hid,))
            self.conn.commit()

        query = "select hid, chain, name, city from hotel where hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteHotelById(self, hid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM hotel WHERE hid = %s"
        cursor.execute(select_query, (hid,))
        hotel = cursor.fetchone()

        if hotel is None:
            cursor.close()
            return None
        else:
            query = "delete from hotel where hid = %s;"
            cursor.execute(query, (hid,))
            self.conn.commit()
            cursor.close()

            cursor.execute("SELECT * FROM hotel")
            result = cursor.fetchall()
            cursor.close()
            return result
