import mysql.connector

mydb=mysql.connector.connect(
     host='localhost',
     user='root',
     password='1703',

)

print(mydb)

mycusor=mydb.cursor()
mycusor.execute("SHOW DATABASES")

for x in mycusor:
    print(x)