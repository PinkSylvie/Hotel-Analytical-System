from flask import jsonify

from config.dbconfig import pg_config
import psycopg2
class StatsDAO:

    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s port=%s host=%s" % \
                         (pg_config['dbname'], pg_config['user'], pg_config['password'],
                          pg_config['dbport'], pg_config['host'])
        print("connection_url: ", connection_url)
        self.conn = psycopg2.connect(connection_url)

# Only Admin have access to Global Stats - Only Returns True or False
    def CheckGlobalAccess(self, eid):

        cursor = self.conn.cursor()
        query = "select eid, position from (employee natural inner join hotel) natural inner join chains where eid = %s"
        cursor.execute(query, (eid,))
        employee = cursor.fetchone()

        if employee:
            eposition = employee[1]  # Second element (employee position)
            if eposition == "Administrator":
                cursor.close()
                return True
        cursor.close()
        return False

# Checks Employee's Access to Local Stats - Only Returns True or False
    def CheckLocalAccess(self, hid, eid):

        cursor = self.conn.cursor()
        query = "select hid, chid from hotel natural inner join chains where hid = %s"
        cursor.execute(query, (hid,))
        hotel = cursor.fetchone()

        if hotel:
            hhid = hotel[0]
            hchid = hotel[1]

            query = "select eid, hid, chid, position from (employee natural inner join hotel) natural inner join chains where eid = %s"
            cursor.execute(query, (eid,))
            employee = cursor.fetchone()

            if employee:
                ehid = employee[1]  # Second element (hotel ID)
                echid = employee[2]  # Third element (chain ID)
                eposition = employee[3]  # Fourth element (employee position)

                if eposition == "Administrator":
                    cursor.close()
                    return True
                elif eposition == "Supervisor":
                    if echid == hchid:
                        cursor.close()
                        return True
                else:
                    if ehid == hhid:
                        cursor.close()
                        return True
        cursor.close()
        return False
# Local Stats
    def getHighestPaid(self, hid):
        cursor = self.conn.cursor()
        query = "select * from employee where hid = %s and position = 'Regular' order by salary desc limit 3;"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

#Global Stats
    def getTopRevenue(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, sum(total_cost) as revenue from (((chains natural inner join hotel) natural inner join room) natural inner join roomunavailable) natural inner join reserve group by chid, cname order by sum(total_cost) desc limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getLeastRooms(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, count(rid) as room_amount from (chains natural inner join hotel) natural inner join room group by chid, cname order by count(rid) limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

