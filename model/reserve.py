from config.dbconfig import pg_config
import psycopg2
class ReserveDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

    def getAllReserve(self):
        cursor = self.conn.cursor()
        query = "select reid, ruid, clid, total_cost, payment, guests from reserve;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def addNewReserve(self,ruid, clid, payment, guests):

        cursor = self.conn.cursor()
        query ="select count(*) from reserve where ruid = %s"
        cursor.execute(query, (ruid,))
        check = cursor.fetchone()[0]
        if check == 0:
            query = "select rprice from room natural inner join roomunavailable where ruid = %s"
            cursor.execute(query,(ruid,))
            total_cost = cursor.fetchone()[0]
            query = "insert into reserve (ruid, clid, total_cost, payment, guests) values (%s, %s, %s, %s, %s);"
            cursor.execute(query, (ruid, clid, total_cost, payment, guests))
            self.conn.commit()
            cursor.execute("SELECT * FROM reserve ORDER BY reid DESC LIMIT 1")
            result = cursor.fetchone()
            cursor.close()
            return result
        else:
            cursor.close()
            return None


    def getReserveById(self, reid):
        cursor = self.conn.cursor()
        query = "select reid, ruid, clid, total_cost, payment, guests from reserve where reid = %s;"
        cursor.execute(query, (reid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def updateReserveById(self, reid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update reserve set"

            if key == "ruid":
                query += " ruid = %s where reid = %s;"
            elif key == "clid":
                query += " clid = %s where reid = %s;"
            elif key == "total_cost":
                query += " total_cost = %s where reid = %s;"
            elif key == "payment":
                query += " payment = %s where reid = %s;"
            else:
                query += " guests = %s where reid = %s;"
            cursor.execute(query, (value,reid,))
            self.conn.commit()

        query = "select reid, ruid, clid, total_cost, payment, guests from reserve where reid = %s;"
        cursor.execute(query, (reid,))
        result = cursor.fetchone()
        cursor.close()
        return result

    def deleteReserveById(self, reid):
        cursor = self.conn.cursor()
        select_query = "SELECT * FROM reserve WHERE reid = %s"
        cursor.execute(select_query, (reid,))
        employee = cursor.fetchone()

        if employee is None:
            cursor.close()
            return None
        else:
            query = "delete from reserve where reid = %s;"
            cursor.execute(query, (reid,))
            # determine affected rows
            affected_rows = cursor.rowcount
            self.conn.commit()
            result = reid
            cursor.close()
            return result

