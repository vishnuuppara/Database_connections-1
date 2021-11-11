import mysql.connector

myconnection = mysql.connector.connect(
    host="localhost",
    user ="root",
    password="knack@321"
)

Dbconnection = myconnection.cursor()

Dbconnection.execute("Show Databases")
print("Following are the available databases :")
for db in Dbconnection:
    print(db)

