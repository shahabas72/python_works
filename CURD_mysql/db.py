import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="database_2"
)
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE database_2")
mycursor.execute("CREATE TABLE employee (emp_id INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50), password VARCHAR(10), phone_number INTEGER, email VARCHAR(30))")