import mysql.connector
def connect_database():
    mydb = mysql.connector.connect(
        host= 'localhost',
        user= 'root',
        password='',
        database='lesson8_student'
    )
    return mydb

def get_address():
    mydb = connect_database()
    sql = 'SELECT * FROM address'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_birth_date():
    mydb = connect_database()
    sql = 'SELECT * FROM birth_date'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_full_name():
    mydb = connect_database()
    sql = 'SELECT * FROM full_name'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_subject():
    mydb = connect_database()
    sql = 'SELECT * FROM subject'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_student():
    mydb = connect_database()
    sql = 'SELECT * FROM student'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()

def get_register():
    mydb = connect_database()
    sql = 'SELECT * FROM register'
    cursor = mydb.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
def find_address_by_data(wards, district, city):
    conn = connect_database()
    sql = f'SELECT * FROM address ' \
          f'WHERE wards =\'{wards}\' ' \
          f'AND district = \'{district}\' ' \
          f'AND city = \'{city}\''
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    row = my_cursor.fetchone()
    return row

def insert_address(data):
    find_row = find_address_by_data(data[0],data[1],data[2])
    if find_row is not None and len(find_row):
        return find_row[0] #nếu tồn tại trả về id
    else:
        mydb = connect_database()
        sql = 'INSERT INTO address(wards,district,city)\
            VALUES(%s,%s,%s)'
        cursor = mydb.cursor()
        cursor.execute(sql,data)
        mydb.commit()
        sql2 = 'SELECT MAX(id) FROM address'
        cursor.execute(sql2)
        row = cursor.fetchone()
        return row[0]

def find_birth_date_by_data(day,month,year):
    mydb = connect_database()
    sql = 'SELECT * FROM birth_date '\
        f'WHERE day = \'{day}\' '\
        f'AND month = {month} '\
        f'AND year = {year}'
    cur = mydb.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    return r
def insert_birth(data):
    row = find_birth_date_by_data(data[0],data[1],data[2])
    if row is not None and len(row):
        return row[0]
    mydb = connect_database()
    sql = 'INSERT INTO birth_date(day,month,year) \
            VALUES(%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
    sql2 = 'SELECT MAX(id) FROM birth_date'
    cur.execute(sql2)
    row = cur.fetchone()
    return row[0]

def find_full_name_by_data(first,mid,last):
    mydb = connect_database()
    sql = 'SELECT * FROM full_name '\
        f'WHERE first_name =\'{first}\' '\
        f'AND mid_name = \'{mid}\' '\
        f'AND last_name = \'{last}\''
    cur = mydb.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    return r
def insert_full_name(data):
    row = find_full_name_by_data(data[0],data[1],data[2])
    if row is not None and len(row):
        return row[0]
    mydb = connect_database()
    sql = 'INSERT INTO full_name(first_name,mid_name,last_name) \
            VALUES(%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
    sql2 = 'SELECT MAX(id) FROM full_name'
    cur.execute(sql2)
    row = cur.fetchone()
    return row[0]

def is_recourd_existed(table_name,colunm_name,id):
    mydb = connect_database()
    sql = f'SELECT * FROM {table_name} '\
        f'WHERE {colunm_name} = \'{id}\' '
    cur = mydb.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    if r is None:
        return False
    return True

def insert_student(data):
    if is_recourd_existed('student','student_id',data[0]):
        return
    else:
        conn = connect_database()
        sql = 'INSERT INTO student(student_id, person_id, full_name_id' \
              ', address_id, birth_date_id, email, gpa, major) ' \
              'VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        my_cursor = conn.cursor()
        my_cursor.execute(sql, data)
        conn.commit()
def insert_subject(data):
    if is_recourd_existed('subject','id',data[0]):
        return
    else:
        conn = connect_database()
        sql = 'INSERT INTO subject(id, name, credit)' \
              'VALUES(%s, %s, %s)'
        my_cursor = conn.cursor()
        my_cursor.execute(sql, data)
        conn.commit()
def is_register_existed(student_id,subject_id):
    mydb = connect_database()
    sql = 'SELECT * FROM register WHERE '\
        f'student_id = \'{student_id}\''\
        f'AND subject_id = \'{subject_id}\''
    cur = mydb.cursor()
    cur.execute(sql)
    r = cur.fetchone()
    if r is not None:
        return True
    return False

def insert_register(data):
    if is_recourd_existed('register','id',data[0]):
        return
    if is_register_existed(data[1],data[2]):
        return
    mydb = connect_database()
    sql = 'INSERT INTO register(id,student_id,subject_id,register_time)'\
            'VALUES(%s,%s,%s,%s)'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
    print('INSERT SUCCESS')

def static_subject():
    """
        Hàm thống kê số lượng đăng ký theo từng môn học.
        Sx giảm dần theo số lượng đk
        :return: danh sách kết quả thống kê đc
        """
    conn = connect_database()
    sql = f'SELECT s.id, s.name, COUNT(r.student_id) AS number_register ' \
          f'FROM register r, subject s ' \
          f'WHERE r.subject_id=s.id ' \
          f'GROUP BY s.id, s.name ' \
          f'ORDER BY number_register DESC;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc

def static_student_by_city():
    """
        Hàm thống kê số lượng sinh viên theo từng thaành ph.
        Sx giảm dần theo số lượng đk
        :return: danh sách kết quả thống kê đc
        """
    conn = connect_database()
    sql = f'SELECT r.city, COUNT(s.student_id) AS number_student ' \
          f'FROM address r, student s ' \
          f'WHERE r.id=s.address_id ' \
          f'GROUP BY r.city ' \
          f'ORDER BY number_student DESC;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc
def students_gpa_good():
    mydb = connect_database()
    sql = f'SELECT * FROM student WHERE gpa >=3.2 ORDER BY gpa DESC'
    cur = mydb.cursor()
    cur.execute(sql)
    return cur.fetchall()
def student_in_same_city():
    """
    Hàm liệt kê các sv cùng 1 thành phố.
    :return: số lượng sv từng thành phố sx giảm dần
    """
    conn = connect_database()
    sql = 'WITH cities AS (SELECT city FROM address) ' \
          'SELECT a.city, s.* FROM ' \
          'address a INNER JOIN student s ' \
          'ON a.id = s.address_id, cities ' \
          'WHERE a.city = cities.city ' \
          'GROUP BY a.city, s.student_id ' \
          'ORDER BY a.city ASC;'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc
def student_register_soonest():
    mydb = connect_database()
    sql = 'SELECT r.student_id,r.register_time '\
            'FROM register r ORDER BY r.register_time DESC'
    cur = mydb.cursor()
    cur.execute(sql)
    return cur.fetchmany(5)

def find_second_max_gpa():
    """
    Hàm tìm danh sách sinh viên có điểm TB cao thứ hai.
    :return: Danh sách sinh viên thỏa mãn
    """
    sql = 'SELECT student_id FROM student ' \
          'where gpa = (' \
          'SELECT MIN(res.gpa) ' \
          'FROM (SELECT gpa FROM student ' \
          'GROUP BY gpa ' \
          'ORDER BY gpa DESC ' \
          'LIMIT 2) res' \
          ');'
    conn = connect_database()
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()

def student_gpa_highest():
    mydb = connect_database()
    sql = 'SELECT * '\
            'FROM student ORDER BY gpa DESC'
    cur = mydb.cursor()
    cur.execute(sql)
    return cur.fetchmany(5)
def student_register_many_subject():
    '''Danh sach học sinh đăng ký nhiều môn học nhất'''
    mydb = connect_database()
    sql = 'SELECT student_id, COUNT(*) AS reg_number ' \
          'FROM register ' \
          'GROUP BY student_id ' \
          'HAVING reg_number = (' \
          'SELECT COUNT(*) AS reg_number ' \
          'FROM register r ' \
          'GROUP BY r.student_id ' \
          'ORDER BY reg_number DESC LIMIT 1' \
          ');'
    cur = mydb.cursor()
    cur.execute(sql)
    return cur.fetchall()
def student_zero_register():
    """
    Hàm tìm các sinh viên không đăng ký môn học nào
    :return: danh sách sinh viên thỏa mãn
    """
    conn = connect_database()
    sql = f'SELECT s.student_id ' \
          f'FROM student s ' \
          f'WHERE s.student_id NOT IN ' \
          f'(SELECT student_id FROM register);'
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()  # lấy hết các bản ghi tìm đc

def find_earliest():
    """
    Hàm tìm danh sách bản ghi đăng ký sớm nhất
    :return: danh sách các bản đăng ký sớm nhất
    """
    sql = 'SELECT id FROM register ' \
          'where register_time = (' \
          'SELECT register_time FROM register ' \
          'ORDER BY register_time ASC ' \
          'LIMIT 1' \
          ');'
    conn = connect_database()
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()
def find_latest():
    """
    Hàm tìm danh sách bản ghi đăng ký sớm nhất
    :return: danh sách các bản đăng ký muộn nhất
    """
    sql = 'SELECT id FROM register ' \
          'where register_time = (' \
          'SELECT register_time FROM register ' \
          'ORDER BY register_time DESC ' \
          'LIMIT 1' \
          ');'
    conn = connect_database()
    my_cursor = conn.cursor()
    my_cursor.execute(sql)
    return my_cursor.fetchall()

def update_student_name_db(old, name):
    '''Cập nhật tên sinh viên'''
    r = find_full_name_by_data(old[0],old[1],old[2])
    mydb = connect_database()
    sql = f'UPDATE full_name SET first_name= %s, mid_name = %s,'\
        f'last_name = %s WHERE id = \'{r[0]} \''
    cur = mydb.cursor()
    cur.execute(sql,name)
    mydb.commit()

def update_student_gpa_db(data):
    mydb = connect_database()
    sql = f'UPDATE student SET gpa = %s WHERE student_id = %s'
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()

def update_student_birth_date_db(old,new):
    mydb = connect_database()
    r = find_birth_date_by_data(old[0],old[1],old[2])
    sql = f'UPDATE birth_date SET day = %s, month = %s,year = %s ' \
          f' WHERE id = %s'
    data = (new[0],new[1],new[2],r[0])
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
def update_subject_credit_db(cre,id):
    mydb = connect_database()
    sql = f'UPDATE subject SET credit = %s WHERE id = %s'
    data = (cre,id)
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
def update_student_address_db(old,new):
    mydb = connect_database()
    r = find_address_by_data(old[0],old[1],old[2])
    sql = f'UPDATE address SET wards = %s, district = %s,city = %s ' \
          f' WHERE id = %s'
    data = (new[0],new[1],new[2],r[0])
    cur = mydb.cursor()
    cur.execute(sql,data)
    mydb.commit()
def update_subject_register_db(sub_id,stu_id,old):
    mydb = connect_database()
    sql = 'UPDATE register SET subject_id = %s WHERE student_id = %s AND subject_id = %s '
    cur = mydb.cursor()
    data = (int(sub_id),stu_id,old)
    cur.execute(sql,data)
    mydb.commit()

def delete_subject_db(id):
    mydb = connect_database()
    sql = 'DELETE FROM subject WHERE id = %s'
    cur = mydb.cursor()
    cur.execute(sql,id)
    mydb.commit()
    sql2 = 'DELETE FROM register WHERE subject_id = %s'
    cur.execute(sql2, id)
    mydb.commit()
def delete_subject_register_db(sub_id,stu_id):
    mydb = connect_database()
    sql = 'DELETE FROM register  WHERE student_id = %s AND subject_id = %s '
    cur = mydb.cursor()
    data = (stu_id,sub_id)
    cur.execute(sql,data)
    mydb.commit()
def delete_student_by_last_name_db(last_name):
    mydb = connect_database()
    sql = f'SELECT id FROM full_name WHERE last_name = \'{last_name}\''
    cur = mydb.cursor()
    cur.execute(sql)
    data = cur.fetchall()

    for i in data: # xóa regisster
        get_student_id = f'SELECT student_id FROM student WHERE full_name_id = %s'
        cur.execute(get_student_id, i)
        id_student = cur.fetchone()
        sql_delete_register = 'DELETE FROM register WHERE student_id = %s'
        cur.execute(sql_delete_register,id_student)
        mydb.commit()

    for i in data:# xóa full name address
        sql2 = 'DELETE FROM student WHERE full_name_id = %s'
        cur.execute(sql2,i)
        mydb.commit()


    sql3 = f'DELETE FROM full_name WHERE last_name = \'{last_name}\''
    cur.execute(sql3)
    mydb.commit()





