from config.dbconfig import pg_config
import psycopg2


class ClientDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllClients(self):
        cursor = self.conn.cursor()
        query = "select clid, fname, lname, age, memberyear from client;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getClientById(self, clid):
        cursor = self.conn.cursor()
        # Remember to update chain to chains (testing deletes with extra table)
        query = "select clid, fname, lname, age, memberyear from client where clid = %s;"
        cursor.execute(query, (clid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewClient(self, fname, lname, age, memberyear):

        cursor = self.conn.cursor()
        query = "insert into client (fname, lname, age, memberyear) values (%s, %s, %s, %s);"
        cursor.execute(query, (fname, lname, age, memberyear))
        self.conn.commit()
        cursor.execute("SELECT * FROM client")
        result = cursor.fetchall()
        cursor.close()
        return result

    def updateClientById(self, clid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update client set"

            if key == "fname":
                query += " fname = %s where clid = %s;"
            elif key == "lname":
                query += " lname = %s where clid = %s;"
            elif key == "age":
                query += " age = %s where clid = %s;"
            else:
                query += " memberyear = %s where clid = %s;"
            cursor.execute(query, (value, clid,))
            self.conn.commit()
        query = "select clid, fname, lname, age, memberyear from client where clid = %s;"
        cursor.execute(query, (clid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteClientById(self, clid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM client WHERE clid = %s"
        cursor.execute(select_query, (clid,))
        client = cursor.fetchone()

        if client is None:
            cursor.close()
            return None
        else:
            query = "delete from client where clid = %s;"
            cursor.execute(query, (clid,))
            self.conn.commit()
            cursor.close()

            cursor.execute("SELECT * FROM client")
            result = cursor.fetchall()
            cursor.close()
            return result

