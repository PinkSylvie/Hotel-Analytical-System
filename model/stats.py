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
        query = "select eid, position \
                 from (employee natural inner join hotel) natural inner join chains \
                 where eid = %s"
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
        query = "select hid, chid \
                 from hotel natural inner join chains \
                 where hid = %s"
        cursor.execute(query, (hid,))
        hotel = cursor.fetchone()

        if hotel:
            hhid = hotel[0]
            hchid = hotel[1]

            query = "select eid, hid, chid, position \
                     from (employee natural inner join hotel) natural inner join chains \
                     where eid = %s"
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

    def getLeastReserve(self, hid):
        cursor = self.conn.cursor()
        query = "select ruid, rid, startdate, enddate, daterange_subdiff(enddate, startdate) as days_unavailable \
                 from roomunavailable natural inner join room \
                 where hid = %s \
                 order by days_unavailable ASC \
                 limit 3"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getRoomType(self, hid):
        cursor = self.conn.cursor()
        query = ("select rtype, count(reid) as reserved\
                 from hotel natural inner join room natural inner join roomunavailable  natural inner join reserve natural inner join roomdescription\
                 where hid = %s \
                 group by rtype\
                 order by reserved")
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    
    def getLeastGuests(self, hid):
        cursor = self.conn.cursor()
        query = ("WITH room_reservation_stats AS ( \
                 SELECT rid, SUM(guests) AS total_guests, \
                 capacity * COUNT(rid) AS total_capacity_reserved \
                 FROM room \
                 NATURAL INNER JOIN roomunavailable \
                 NATURAL INNER JOIN reserve \
                 NATURAL INNER JOIN roomdescription \
                 where hid = %s \
                 GROUP BY rid, capacity ) \
                 SELECT rid, round(cast(total_guests as numeric)/total_capacity_reserved, 2) as ratio \
                 FROM room_reservation_stats \
                 ORDER BY ratio \
                 limit 3;")
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getHighestPaid(self, hid):
        cursor = self.conn.cursor()
        query = "select * \
                 from employee \
                 where hid = %s and position = 'Regular' \
                 order by salary desc \
                 limit 3;"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getTopClientDiscount(self, hid):
        cursor = self.conn.cursor()
        # If this returns an error remove single quotes from columns
        query = "select distinct clid, fname, lname, age, memberyear, \
        case when memberyear between 1 and 4 then 2 \
        when memberyear between 5 and 9 then 5 \
        when memberyear between 10 and 14 then 8 else 12 \
        end as discount \
        from (client natural inner join reserve) natural inner join (roomunavailable natural inner join room) \
        natural inner join hotel \
        where hid = %s order by memberyear desc limit 5;"

        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getTopCreditClient(self, hid):
        cursor = self.conn.cursor()
        # If this returns an error remove single quotes from columns
        query = "select clid, fname, lname, count(reserve.clid) as reservation_count \
                 from client natural inner join reserve natural inner join roomunavailable natural inner join room natural inner join hotel \
                 where client.age < 30 and payment = 'credit card' and hid = %s \
                 group by clid, fname, lname \
                 order by reservation_count desc \
                 limit 5;"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result
    
    def getMostReservedHandicap(self, hid):
        cursor = self.conn.cursor()
        query = "select rid, hid, rname, rtype, ishandicap, count(*) as total_reservations \
                 from reserve natural inner join roomunavailable natural inner join room natural inner join  roomdescription \
                where ishandicap = true and hid = %s \
                group by rid, rid, hid, rname, rtype, ishandicap \
                order by total_reservations DESC \
                limit 5;"
        cursor.execute(query, (hid,))
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    # Global Stats---------------------------------------------------------------------------------------------------
    def getTopRevenue(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, sum(total_cost) as revenue \
                 from (((chains natural inner join hotel) natural inner join room) natural inner join roomunavailable) natural inner join reserve \
                 group by chid, cname \
                 order by sum(total_cost) desc \
                 limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getLeastRooms(self):
        cursor = self.conn.cursor()
        query = "select chid, cname, count(rid) as room_amount \
                 from (chains natural inner join hotel) natural inner join room \
                 group by chid, cname \
                 order by count(rid) \
                 limit 3;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getTopHotelCap(self):
        cursor = self.conn.cursor()
        query = "select hid, hname, hcity, sum(capacity) as total_cap \
                 from hotel natural inner join room natural inner join roomdescription \
                 group by hid, hname, hcity \
                 order by total_cap desc \
                 limit 5;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getTopHotelRes(self):
        cursor = self.conn.cursor()
        query = "WITH HotelReservationCounts AS (SELECT h.hid, h.hname, h.hcity, COUNT(ru.ruid) AS reservation_count FROM hotel h INNER JOIN room r ON h.hid = r.hid LEFT JOIN roomunavailable ru ON r.rid = ru.rid GROUP BY h.hid, h.hname, h.hcity), RankedHotels AS (SELECT *, (PERCENT_RANK() OVER (ORDER BY reservation_count DESC)) * 100 AS percentile_rank FROM HotelReservationCounts) SELECT * FROM RankedHotels WHERE percentile_rank <= 10;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getPaymentMethod(self):
        cursor = self.conn.cursor()
        query = "SELECT payment, count(*) as total_reservations, count(*)* 100.0/ sum(count(*)) over () as percent\
                 from reserve \
                 group by payment"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

    def getProfitMonth(self):
        cursor = self.conn.cursor()
        query = "with profitmonth as( \
                        SELECT cname, \
                        extract(Month from startdate) as reservation_month, \
                        count(*) as total_reservation, \
                        row_number() over (partition by cname order by count(*) desc) as month_rank \
                        from reserve \
                        natural inner join roomunavailable \
                        natural inner join room \
                        natural inner join hotel \
                        natural inner join chains \
                        group by cname, reservation_month) \
                 select cname, reservation_month, total_reservation \
                 from profitmonth \
                 where month_rank <= 3"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        cursor.close()
        return result

