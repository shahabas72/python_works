import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='database3'
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE database3")
#mycursor.execute("""
#    CREATE TABLE bank (
#        account_no BIGINT PRIMARY KEY AUTO_INCREMENT,
#        account_name VARCHAR(30),
#        amount DECIMAL(10, 2),
#        balance DECIMAL(10, 2)
#    )
#""")

#mycursor.execute("ALTER TABLE bank AUTO_INCREMENT = 100000000"
mycursor.execute("ALTER TABLE bank MODIFY COLUMN balance DECIMAL (10, 2) DEFAULT 0.00")
