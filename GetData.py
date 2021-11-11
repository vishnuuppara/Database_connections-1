import mysql.connector



myconnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "knack@321",
    database = "sharan"
)

Dbconnection = myconnection.cursor()
sql_query = "select * from my_info"
Dbconnection.execute(sql_query)



for data in Dbconnection:
    print(data)