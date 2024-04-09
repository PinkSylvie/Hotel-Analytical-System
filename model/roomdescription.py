from config.dbconfig import pg_config
import psycopg2

class RoomdescriptionDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllRoomdescriptions(self):
        cursor = self.conn.cursor()
        query = "select rdid, rname, rtype, capacity, ishandicap from roomdescription;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRoomdescriptionById(self, rdid):
        cursor = self.conn.cursor()
        query = "select rdid, rname, rtype, capacity, ishandicap from roomdescription where rdid = %s;"
        cursor.execute(query, (rdid,))
        result = cursor.fetchone()
        return result
    
    def addRoomdescription(self, rdid, rname, rtype, capacity, ishandicap):

        cursor = self.conn.cursor()
        query = "insert into roomdescription (rdid, rname, rtype, capacity, ishandicap) values (%s, %s, %s, %s, %s);"
        cursor.execute(query, (rdid, rname, rtype, capacity, ishandicap))
        self.conn.commit()
        cursor.execute("SELECT * FROM roomdescription")
        result = cursor.fetchall()
        cursor.close()
        return result

    def deleteRoomdescriptionById(self, rdid):
        cursor = self.conn.cursor()
        query = "delete from roomdescription where rdid = %s;"
        cursor.execute(query, (rdid,))
        result = cursor.fetchone()
        return result
    
    def updateRoomdescriptionById(self, rdid, data):
        cursor = self.conn.cursor()
        
        for key, value in data.items():
            query = "update roomdescription set"

            if key == "rdid":
                query += " rdid = %s where rdid = %s;"
            elif key == "rname":
                query += " rname = %s where rdid = %s;"
            elif key == "rtype":
                query += " rtype = %s where rdid = %s;"
            elif key == "capacity":
                query += " capacity = %s where rdid = %s;"
            else:
                query += " ishandicap = %s where rdid = %s;"
            cursor.execute(query, (value, rdid,))
            self.conn.commit()
        query = "select rdid, rname, rtype, capacity, ishandicap from roomdescription where rdid = %s;"
        cursor.execute(query, (rdid,))
        result = cursor.fetchone()
        cursor.close()
        return result