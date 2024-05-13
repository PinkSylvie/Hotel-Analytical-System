from config.dbconfig import pg_config
import psycopg2


class RoomDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllRooms(self):
        cursor = self.conn.cursor()
        query = "select rid, hid, rdid, rprice from room;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getRoomById(self, rid):
        cursor = self.conn.cursor()
        query = "select rid, hid, rdid, rprice from room where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewRoom(self, hid, rdid, rprice):

        cursor = self.conn.cursor()
        query = "insert into room (hid, rdid, rprice) values (%s, %s, %s);"
        cursor.execute(query, (hid, rdid, rprice))
        self.conn.commit()
        query = "SELECT * FROM room ORDER BY ruid DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def updateRoomById(self, rid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update room set"

            if key == "hid":
                query += " hid = %s where rid = %s;"
            elif key == "rdid":
                query += " rdid = %s where rid = %s;"
            else:
                query += " rprice = %s where rid = %s;"
            cursor.execute(query, (value, rid,))
            self.conn.commit()

        query = "select rid, hid, rdid, rprice from room where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteRoomById(self, rid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM room WHERE rid = %s"
        cursor.execute(select_query, (rid,))
        room = cursor.fetchone()

        if room is None:
            cursor.close()
            return None
        else:
            query = "delete from room where rid = %s;"
            cursor.execute(query, (rid,))
            affected_rows = cursor.rowcount
            self.conn.commit()
            result = rid
            cursor.close()
            return result
