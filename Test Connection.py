import mysql.connector

myconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="knack@321"

)
Dbconnection = myconnection.cursor()
print("Database connected successfully")
myconnection.close()
print("Database disconnected successfully")

