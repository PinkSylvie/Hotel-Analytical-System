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
        cursor.close()
        return result

    def addNewEmployee(self,hid,fname,lname,age,position,salary):

        cursor = self.conn.cursor()
        query = "insert into employee (hid,fname,lname,age,position,salary) values (%s, %s, %s, %s, %s, %s);"
        cursor.execute(query, (hid,fname,lname,age,position,salary))
        self.conn.commit()
        query = "select * from employee order by eid desc limit 1"
        cursor.execute(query)
        result = cursor.fetchone()
        cursor.close()
        return result


    def getEmployeeById(self, eid):
        cursor = self.conn.cursor()
        query = "select eid, hid, fname, lname, age, position, salary from employee where eid = %s;"
        cursor.execute(query, (eid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def updateEmployeeById(self, eid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update employee set"

            if key == "hid":
                query += " hid = %s where eid = %s;"
            elif key == "fname":
                query += " fname = %s where eid = %s;"
            elif key == "lname":
                query += " lname = %s where eid = %s;"
            elif key == "age":
                query += " age = %s where eid = %s;"
            elif key == "position":
                query += " position = %s where eid = %s;"
            else:
                query += " salary = %s where eid = %s;"
            cursor.execute(query, (value,eid,))
            self.conn.commit()
        #Remember to update chain to chains (testing deletes with extra table)
        query = "select eid, hid, fname, lname, age, position, salary from employee where eid = %s;"
        cursor.execute(query, (eid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteEmployeeById(self, eid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM employee WHERE eid = %s"
        cursor.execute(select_query, (eid,))
        employee = cursor.fetchone()

        if employee is None:
            cursor.close()
            return None
        else:
            query = "delete from employee where eid = %s;"
            cursor.execute(query, (eid,))
            # determine affected rows
            affected_rows = cursor.rowcount
            self.conn.commit()
            result = eid
            cursor.close()
            return result

