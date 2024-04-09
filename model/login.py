from config.dbconfig import pg_config
import psycopg2
class LoginDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllLogins(self):
        cursor = self.conn.cursor()
        query = "select lid, eid, username, password from login;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getLoginById(self, lid):
        cursor = self.conn.cursor()
        query = "select lid, eid, username, password from login where lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        return result