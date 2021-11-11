import mysql.connector

myconnection  = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "knack@321",
    database="sharan"
)

Dbconnection = myconnection.cursor()
sql_query1 = "insert into my_info values(4,'Chey',25,'Atp')"
Dbconnection.execute(sql_query1)
myconnection.commit()

print("Record is inserted successfully")
myconnection.close()
