import mysql.connector
def print_arr(srr):
    for i in srr:
        print(i)
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="",
    database= 'student_register'
)

sql = 'SELECT * FROM student '
mycursor = mydb.cursor()
mycursor.execute(sql)
result =mycursor.fetchall()

print_arr(result)