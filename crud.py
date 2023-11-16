import mysql.connector

try:
        conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='250902',
                database='indigo'
        )
        mycursor = conn.cursor()
        print("Connection Established")
except:
        print("Connection Failed ")

# Create a database on the db server
# mycursor.execute("Create database indigo")
# conn.commit()

# Creating a table (airport -> airport_id,code,name)
# mycursor.execute("""
#         CREATE TABLE airport(
#         airport_id INTEGER PRIMARY KEY,
#         code VARCHAR(10) NOT NULL,
#         city VARCHAR(50) NOT NULL,
#         name VARCHAR(255) NOT NULL
#         )
# """)
# conn.commit()

# Insert data to the table
# mycursor.execute("""
# INSERT INTO airport values
# (1,'DEL','New Delhi','IGIA'),
# (2,'CCU','Kolkata','NSCA'),
# (3,'BOM','Mumbia','CSMA')
# """)
# conn.commit()


# search/retrieve
# mycursor.execute("select * from airport where airport_id>1")
# data = mycursor.fetchall()
# for i in data:
#     print(i[3])

# update
# mycursor.execute("""
# update airport set city = 'Bombay' where airport_id = 3
# """)
# conn.commit()
# mycursor.execute("select * from airport")
# data = mycursor.fetchall()
# print(data)


# delete
# mycursor.execute("delete from airport where airport_id=3")
# conn.commit()
mycursor.execute("select * from airport")
data = mycursor.fetchall()
print(data)