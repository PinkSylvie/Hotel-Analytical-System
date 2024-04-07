from config.dbconfig import pg_config
import psycopg2


class RoomUnavailableDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
        (pg_config['dbname'], pg_config['user'], pg_config['password'],
         pg_config['port'], pg_config['host'])
        print(connection_url)
        self.conn = psycopg2.connect(connection_url)
        
    def getAllRoomUnavailable(self):
        cursor = self.conn.cursor()
        query = "select ruid, rid, startdate, enddate \
                 from roomunavailable;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
    
    def getRoomUnavailableByRuid(self, ruid):
        cursor = self.conn.cursor()
        query = "select ruid, rid, startdate, enddate \
                 from roomunavailable \
                 where ruid=%s;"
        cursor.execute(query, (ruid,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def addNewRoomUnavailable(self, rid, startdate, enddate):
        cursor = self.conn.cursor()
        query = "insert into roomunavailable (rid, startdate, enddate) values (%s, %s, %s);"
        cursor.execute(query, (rid, startdate, enddate))
        self.conn.commit()
        cursor.execute("SELECT * \
                        FROM roomunavailable")
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def updateRoomUnavailableByRuid(self, ruid, data):
        cursor = self.conn.cursor()

        for key, value in data.items():
            query = "update roomunavailable set"

            if key == "rid":
                query += " rid = %s where ruid = %s;"
            elif key == "startdate":
                query += " startdate = %s where ruid = %s;"
            else:
                query += " enddate = %s where ruid = %s;"
                
            cursor.execute(query, (value, ruid,))
            self.conn.commit()
            
        query = "select * \
                 from roomunavailable \
                 where ruid = %s;"
        cursor.execute(query, (ruid,))
        result = cursor.fetchone()
        cursor.close()
        return result
    
    def deleteRoomUnavailableByRuid(self, ruid):
        cursor = self.conn.cursor()
        select_query = "select * \
                        from roomunavailable \
                        where ruid = %s"
        cursor.execute(select_query, (ruid,))
        roomunavailable = cursor.fetchone()

        if roomunavailable is None:
            cursor.close()
            return None
        else:
            query = "delete from roomunavailable \
                     where ruid = %s;"
            cursor.execute(query, (ruid,))
            self.conn.commit()
            cursor.execute("SELECT * \
                            FROM roomunavailable")
            result = cursor.fetchall()
            cursor.close()
            return result