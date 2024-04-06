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
        query = "select hid, chid, hname, hcity from hotel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getHotelById(self, hid):
        cursor = self.conn.cursor()
        query = "select hid, chid, hname, hcity where hid = %s;"
        cursor.execute(query, (hid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewHotel(self, chid, hname, hcity):

        cursor = self.conn.cursor()
        query = "insert into hotel (chid, hname, hcity) values (%s, %s, %s);"
        cursor.execute(query, (chid, hname, hcity))
        self.conn.commit()
        cursor.execute("SELECT * FROM hotel")
        result = cursor.fetchall()
        cursor.close()
        return result

    def updateHotelById(self, hid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update hotel set"

            if key == "chid":
                query += " chid = %s where hid = %s;"
            elif key == "hname":
                query += " hname = %s where hid = %s;"
            else:
                query += " hcity = %s where hid = %s;"
            cursor.execute(query, (value, hid,))
            self.conn.commit()

        query = "select hid, chid, hname, hcity from hotel where hid = %s;"
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
