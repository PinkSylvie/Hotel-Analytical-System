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
    
    def addNewLogin(self, lid, employee_id_value, username_value, password_value):
        cursor = self.conn.cursor()
        query = "insert into login (eid, username, password) values (employee_id_value, 'username_value', 'password_value');"
        cursor.execute(query, (lid, employee_id_value, username_value, password_value))
        self.conn.commit()
        cursor.execute("SELECT * FROM login")
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def updateLoginById(self, lid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update login set"

            if key == "password":
                query += " password = %s where lid = %s;"
            elif key == "username":
                query += " username = %s where lid = %s;"
            elif query == "eid":
                query += " eid = %s where lid = %s;"
            cursor.execute(query, (value, lid,))
            self.conn.commit()
        query = "select eid, username, password from login where lid = %s"
        cursor.execute(query, (lid, ))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def deleteLoginById(self, lid):
        cursor = self.conn.cursor()
        query = "delete from login where username = %s"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        return result
