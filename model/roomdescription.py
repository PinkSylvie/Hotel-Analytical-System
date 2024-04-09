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
    
    def addRoomdescription(self, fname, lname, age, memberyear):

        cursor = self.conn.cursor()
        query = "insert into client (fname, lname, age, memberyear) values (%s, %s, %s, %s);"
        cursor.execute(query, (fname, lname, age, memberyear))
        self.conn.commit()
        cursor.execute("SELECT * FROM client")
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
            query = "update room description"

            if key == "rid":
                query += " rid = %s where rid = %s;"
            elif key == "rname":
                query += " rname = %s where rid = %s;"
            elif key == "rtype":
                query += " rtype = %s where rid = %s;"
            elif key == "capacity":
                query += " capacity = %s where rid = %s;"
            else:
                query += " ishandicap = %s where rid = %s;"
            cursor.execute(query, (value, rdid,))
            self.conn.commit()
        query = "select rdid, fname, lname, age, memberyear from client where clid = %s;"
        cursor.execute(query, (rdid,))
        result = cursor.fetchone()
        cursor.close()
        return result