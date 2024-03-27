from config.dbconfig import pg_config
import psycopg2
class EmployeeDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllEmployees(self):
        cursor = self.conn.cursor()
        query = "select eid, hid, fname, lname, age, position, salary from employee;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEmployeeById(self, eid):
        cursor = self.conn.cursor()
        query = "select eid, hid, fname, lname, age, position, salary from employee where eid = %s;"
        cursor.execute(query, (eid,))
        result = cursor.fetchone()
        return result