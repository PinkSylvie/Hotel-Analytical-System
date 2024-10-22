from config.dbconfig import pg_config
import psycopg2


class LoginDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getValidLogin(self, username, password):
        cursor = self.conn.cursor()
        query = "select lid, eid, username, password, position from login natural inner join employee where username = %s and password = %s;"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return result

    def signUp(self, hid, fname, lname, age, position, salary, username_value, password_value):

        cursor = self.conn.cursor()
        query = "SELECT COUNT(*) FROM login WHERE username = %s"
        cursor.execute(query, (username_value,))
        duplicate = cursor.fetchone()[0]
        if duplicate > 0:
            cursor.close()
            return None

        query = "insert into employee (hid,fname,lname,age,position,salary) values (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (hid, fname, lname, age, position, salary))
        self.conn.commit()

        query = "select eid from employee order by eid desc limit 1"
        cursor.execute(query)
        seid = cursor.fetchone()[0]
        query = "insert into login (eid, username, password) values (%s, %s, %s);"
        cursor.execute(query, (seid, username_value, password_value))
        self.conn.commit()

        cursor.execute("SELECT lid FROM login ORDER BY lid DESC LIMIT 1;")
        lid = cursor.fetchone()[0]
        query = "select lid, eid, username, password, position from login natural inner join employee where lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def getAllLogins(self):
        cursor = self.conn.cursor()
        query = "select lid, eid, username, password from login;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getLoginById(self, lid):
        cursor = self.conn.cursor()
        query = "select lid, eid, username, password from login where lid = %s;"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def addNewLogin(self, employee_id_value, username_value, password_value):
        cursor = self.conn.cursor()
        query ="select count(*) from login where eid = %s"
        cursor.execute(query, (employee_id_value,))
        check = cursor.fetchone()[0]
        if check == 0:
            query = "insert into login (eid, username, password) values (%s, %s, %s);"
            cursor.execute(query, (employee_id_value, username_value, password_value))
            self.conn.commit()
            cursor.execute("SELECT * FROM login ORDER BY lid DESC LIMIT 1")
            result = cursor.fetchone()
            cursor.close()
            return result
        else:
            cursor.close()
            return None


    def updateLoginById(self, lid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update login set"

            if key == "password":
                query += " password = %s where lid = %s;"
            elif key == "username":
                query += " username = %s where lid = %s;"
            elif key == "eid":
                query += " eid = %s where lid = %s;"
            cursor.execute(query, (value, lid,))
            self.conn.commit()
        query = "select lid, eid, username, password from login where lid = %s"
        cursor.execute(query, (lid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteLoginById(self, lid):
        cursor = self.conn.cursor()
        select_query = "select * from login where lid = %s;"
        cursor.execute(select_query, (lid,))
        login = cursor.fetchone()

        if login is None:
            cursor.close()
            return None
        else:
            query = "delete from login where lid = %s"
            cursor.execute(query, (lid,))
            self.conn.commit()
            # cursor.execute("SELECT * FROM login")
            # result = cursor.fetchall()
            result = lid
            cursor.close()
            return result