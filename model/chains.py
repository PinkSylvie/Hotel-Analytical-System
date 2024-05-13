from config.dbconfig import pg_config
import psycopg2
class ChainsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllChains(self):
        cursor = self.conn.cursor()
        query = "select * from chains;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getChainById(self, chid):
        cursor = self.conn.cursor()

        query = "select * from chains where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewChain(self, cname, springmkup,summermkup,fallmkup,wintermkup):

        cursor = self.conn.cursor()
        query = "insert into chains (cname, springmkup, summermkup, fallmkup, wintermkup) values (%s, %s, %s, %s, %s);"
        cursor.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup))
        self.conn.commit()
        query = "select * from chains order by chid desc limit 1"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result

    def updateChainById(self, chid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update chains set"

            if key == "cname":
                query += " cname = %s where chid = %s;"
            elif key == "springmkup":
                query += " springmkup = %s where chid = %s;"
            elif key == "summermkup":
                query += " summermkup = %s where chid = %s;"
            elif key == "fallmkup":
                query += " fallmkup = %s where chid = %s;"
            else:
                query += " wintermkup = %s where chid = %s;"
            cursor.execute(query, (value,chid,))
            self.conn.commit()
        query = "select * from chains where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteChainById(self, chid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM chains WHERE chid = %s"
        cursor.execute(select_query, (chid,))
        chain = cursor.fetchone()

        if chain is None:
            cursor.close()
            return None
        else:
            query = "delete from chains where chid = %s;"
            cursor.execute(query, (chid,))
            self.conn.commit()
            result = chid
            cursor.close()
            return result


