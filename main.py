import mysql.connector

connection= connection = mysql.connector.connect(
    user= 'root',
    database= 'sample',
    password= '2gd4fart'
)

cursor = connection.cursor()
testQuery = ("SELECT * FROM bank_info")
cursor.execute(testQuery)
 

for row in cursor:
    print(row)

cursor.close()
connection.close()
