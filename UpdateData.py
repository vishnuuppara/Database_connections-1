import mysql.connector

myconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "knack@321",
    database = "sharan"

)

Dbconnection = myconnection.cursor()
sql_query = "update  my_info set address = 'USA' where name = 'Sai'"
Dbconnection.execute(sql_query)

myconnection.commit()

print("Record is updated successfully")