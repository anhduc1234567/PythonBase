import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database = 'student_register'
)

# sql = 'SHOW DATABASES'
# sql = 'CREATE DATABASE bank'
# sql = 'SHOW TABLES'
# sql = 'CREATE TABLE subject(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(40) NULL, credit INT NOT NULL)'
sql = 'ALTER TABLE subject ADD COLUMN lesson INT NOT NULL'
mycursor = mydb.cursor()
mycursor.execute(sql)
for i in mycursor:
    print(i)