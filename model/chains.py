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
        return result

    def getChainById(self, chid):
        cursor = self.conn.cursor()
        #Remember to update chain to chains (testing deletes with extra table)
        query = "select chid, cname, springmkup, summermkup, fallmkup, wintermkup from chains where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        return result

    def deleteChainById(self, chid):
        cursor = self.conn.cursor()
        #Remember to update chain to chains (testing deletes with extra table)
        query = "delete from chain where chid = %s;"
        cursor.execute(query, (chid,))
        result = cursor.fetchone()
        return result

    def getAllChainsOld(self):
        result = []
        result.append((1,"Bergaum-Champlin",1.01,1.73,1.52,1.98))
        result.append((2, "Wisozk Inc.", 1.19, 1.21, 1.09, 1.53))
        result.append((3, "Murphy and Boyles", 1.51, 1.1, 1.29, 1.58))
        return result