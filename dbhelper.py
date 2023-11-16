import mysql.connector

class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='250902',
                database='fights'
            )
            self.mycursor = self.conn.cursor()
            print("Connection Established")
        except:
            print("Connection Failed ")
    def fetch_city_names(self):
        city = []
        self.mycursor.execute("""
        select distinct Destination from flights
        union
        select distinct Source from flights
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
        return city

    def fetch_all_flights(self,source,destination):
        self.mycursor.execute("""
        select Airline,Route,Dep_time,Duration,Price from flights where Source = '{}' and Destination = '{}'
        """.format(source,destination))

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_frequency(self):
        airline = []
        frequency = []
        self.mycursor.execute("""
        select Airline,count(*) from flights group by Airline order by count(*) desc
        """)
        data = self.mycursor.fetchall()
        for item in data:
            airline.append(item[0])
            frequency.append(item[1])
        return airline,frequency

    def busy_airport(self):
        city = []
        frequency = []
        self.mycursor.execute("""
        select Source, count(*) from (select Source from flights
        union all select Destination from flights) t group by t.Source order by count(*) desc
        """)
        data = self.mycursor.fetchall()
        for item in data:
            city.append(item[0])
            frequency.append(item[1])
        return city, frequency

    def daily_frequency(self):
        date = []
        frequency = []
        self.mycursor.execute("""
        select Date_of_Journey,count(*) from flights group by Date_of_Journey
        """)
        data = self.mycursor.fetchall()
        for item in data:
            date.append(item[0])
            frequency.append(item[1])
        return date, frequency
