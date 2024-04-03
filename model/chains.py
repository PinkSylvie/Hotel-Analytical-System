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
        query = "select chid, cname, springmkup, summermkup, fallmkup, wintermkup from chain;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getChainById(self, chid):
        cursor = self.conn.cursor()
        #Remember to update chain to chains (testing deletes with extra table)
        query = "select chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewChain(self, cname, springmkup,summermkup,fallmkup,wintermkup):

        cursor = self.conn.cursor()
        query = "insert into chain (cname, springmkup, summermkup, fallmkup, wintermkup) values (%s, %s, %s, %s, %s);"
        cursor.execute(query, (cname, springmkup, summermkup, fallmkup, wintermkup))
        self.conn.commit()
        cursor.execute("SELECT * FROM chain")
        result = cursor.fetchall()
        cursor.close()
        return result

    def updateChainById(self, chid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update chain set"

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
        #Remember to update chain to chains (testing deletes with extra table)
        query = "select chid, cname, springmkup, summermkup, fallmkup, wintermkup from chain where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteChainById(self, chid):
        cursor = self.conn.cursor()
        #Remember to update chain to chains (testing deletes with extra table)
        #DONT TOUCH
        select_query = "SELECT * FROM chain WHERE chid = %s"
        cursor.execute(select_query, (chid,))
        chain = cursor.fetchone()

        if chain is None:
            cursor.close()
            return None
        else:
            query = "delete from chain where chid = %s;"
            cursor.execute(query, (chid,))
            self.conn.commit()
            cursor.close()

            cursor.execute("SELECT * FROM chain")
            result = cursor.fetchall()
            cursor.close()
            return result

    def getTopRevenue(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, sum(total_cost) as revenue from (((chain natural inner join hotel) natural inner join room) natural inner join roomunavailable) natural inner join reserve group by chid, cname order by sum(total_cost) desc limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getLeastRooms(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, count(rid) as room_amount from (chain natural inner join hotel) natural inner join room group by chid, cname order by count(rid) limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
