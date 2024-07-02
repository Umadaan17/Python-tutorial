import mysql.connector

mydb=mysql.connector.connect(
     host='localhost',
     user='root',
     password='1703',
)

mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE if not exists TEST69")
mydb.close()