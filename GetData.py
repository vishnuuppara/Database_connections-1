import mysql.connector

def get_data():

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

Data = get_data()
print(Data)