from  utils import *

students = read_student_from_database()
subjects = read_subject_from_database()
registers = read_register_from_database(students,subjects)
update_autoid_Student(students)

update_autoid_Subject(subjects)
update_autoid_Register(registers)
print(Student.AUTO_ID)
menu = 100
while menu != 0:
    print('======>VUI LÒNG CHỌN CHỨC NĂNG<===========\n'
            '1. Thêm mới sinh viên vào danh sách sinh viên.\n' 
             '2. Thêm mới môn học vào danh sách môn học.\n' 
             '3. Thêm mới bảng đăng ký môn học vào danh sách đăng ký.\n' 
             '4. Sắp xếp danh sách sinh viên theo tên a-z.\n' 
             '5. Sắp xếp danh sách môn học theo tên a-z.\n' 
             '6. Sắp xếp danh sách bảng đăng ký theo thời gian đăng ký.\n' 
             '7. Hiển thị danh sách sinh viên.\n' 
             '8. Hiển thị danh sách môn học.\n'
             '9. Hiển thị danh sách bảng đăng ký.\n' 
             '10. Liệt kê danh sách môn học mà sinh viên đăng ký.\n' 
             '11. Liệt kê danh sách sinh viên đăng ký theo mã môn.\n' 
             '12. Thống kê số lượng sinh viên đăng ký theo từng môn học.\n' 
             '13. Thống kê số lượng sinh viên theo từng thành phố.\n' 
             '14. Liệt kê các sinh viên có điểm TB >= 3.2.\n' 
             '15. Liệt kê các sinh viên cùng tên, cùng thành phố và cùng năm sinh.\n' 
             '16. Liệt kê top 5 sinh viên đăng ký sớm nhất.\n' 
             '17. Liệt kê top 5 sinh viên có điểm TB cao nhất.\n' 
             '18. Tìm các sinh viên có điểm TB cao thứ 2.\n' 
             '19. Liệt kê danh sách các sinh viên đăng ký nhiều môn học nhất.\n' 
             '20. Liệt kê danh sách các sinh viên không đăng ký môn học nào.\n' 
             '21. Cho biết thông tin bản ghi của bản đăng ký sớm nhất.\n' 
             '22. Cho biết thông tin bản ghi của bản đăng ký muộn nhất.\n' 
             '23. Cập nhật họ và tên cho sinh viên theo mã sinh viên. Có xử lý ngoại lệ.\n' 
             '24. Cập nhật điểm cho sinh viên theo mã sinh viên. Có xử lý ngoại lệ.\n' 
             '25. Cập nhật ngày sinh cho sinh viên theo mã sinh viên .\n'
             '26. Cập nhật số tín cho môn học theo mã môn học .\n'
             '27. Cập nhật địa chỉ cho sinh viên theo mã sinh viên .\n'
             '28. Thay đổi môn học cho sinh viên trong bản đăng ký the0 mã sinh viên và mã môn học cũ .\n')
    menu = int(input('=========>CHỌN CHỨC NĂNG<=========  '))
    if menu == 1:
        try:
            print(Student.AUTO_ID)
            new_student = create_student()
            students.append(new_student)
            save_student(new_student)
            print('=====THEM THANH CONG======')
            print(Student.AUTO_ID)
        except ValueError as e:
            print(e)
            print('Lỗi không thành công')
    if menu == 2:
        try:
            new_subject = creat_subject()
            subjects.append(new_subject)
            save_subjetc(new_subject)
            print('====THEM THÀNH CONG====')
        except ValueError as e:
            print(e)
            print('Lỗi không thành công')
    if menu == 3:
        try:
            new_register = creat_register(registers, students, subjects)
            if new_register is not None:
                registers.append(new_register)
                save_registers(new_register)
                print('==> Đăng ký môn học thành công! <==')
            else:
                print('==> Tạo bản đăng ký thất bại.')
        except ValueError as e:
            print(e)
    if menu == 4:
        if len(students) > 0:
            print('===SẮP XẾP DANH SÁCH SINH VIÊN THEO HỌ TÊN TĂNG DẦN')
            students.sort(key=lambda x:(x.full_name.first,x.full_name.last))
        else:
            print('Danh sách rỗng')
    if menu == 5:
        if len(subjects) > 0:
            print('===SẮP XẾP DANH SÁCH MÔN HỌC TĂNG DẦN THEO TÊN===')
            subjects.sort(key=lambda x:(x.subject_name))
        else:
            print('Danh sách rỗng')
    if menu == 6:
        if len(registers) > 0:
            sort_registers(registers)
            print('==> Danh sách đăng ký sau khi sắp xếp: ')
        else:
            print('==> Danh sách đăng ký rỗng <==')
    if menu == 7:
        print('===DANH SÁCH SINH VIÊN LA===')
        print_arr(students)
    if menu == 8:
        print('DANH SÁCH MÔN HỌC LÀ===')
        print_arr(subjects)
    if menu == 9:
        print('DANH SÁCH BẢN ĐĂNG KÝ LÀ===')
        print_arr(registers)
    if menu == 10:
        list_subjects_by_id(subjects,registers)
    if menu == 11:
        list_students_register_subject(registers,students)
    if menu == 12:
        print('===Thông kê số lượng sinh viên đăng ký theo môn học là: =====')
        static_number_subject()
        #static_number_subject_by_dict(registers)
    if menu == 13:
        print('THÔNG KẾ SỐ LƯỢNG SINH VIÊN THEO THÀNH PHỐ')
        static_number_studentscity()
    if menu == 14:
        print('DANH SACH HỌC SINH CÓ ĐIỂM GPA >=3.2 LÀ')
        print_arr(list_student_good())
    if menu == 15:
        print('DANH SÁCH HỌC SINH CHUNG 1 THÀNH PHỐ LÀ:')
        stat_student_same_city()
    if menu == 16:
        print('TOP 5 SINH VIÊN ĐĂNG KÝ SỚM NHẤT LÀ: ')
        list_register_earliest(students)
    if menu == 17:
        print('TOP 5 SINH VIEN CÓ ĐIỂM TRUNG BÌNH CAO NHẤT LÀ')
        list_student_gpa_high(students)
    if menu == 18:
        print('SINH VIEN CÓ DIEM TRUNG BINH CAO THU 2 LA')
        find_students_gpa_nd2(students)
       # stat_scond_max_gpa(students)
    if menu == 19:
        print('DANH SACH SINH VIEN DANG KY NHIEU MON HOC NHẤT')
        list_student_most_reg(students)
    if menu == 20:
        print('DANH SACH SINH VIEN KHONG DANG KY MON HOC LA')
        list_student_zero_reg(students)
    if menu == 21:
        print('THÔNG TIN BẢN ĐĂNG KÝ SỚM NHẤT LÀ')
        find_register_earliest(registers)
    if menu == 22:
        print('THÔNG TIN BẢN ĐĂNG KÝ MUỘN NHẤT LÀ')
        find_register_latest(registers)
    if menu == 23:
        print('CẬP NHẬT HỌ VÀ TÊN CHO SINH VIÊN')
        update_name_by_student_id(students)
    if menu == 24:
        print('CẬP NHẬT GPA CHO SINH VIÊN')
        update_gpa_by_student_id(students)
    if menu == 25:
        print('CẬP NHẬT NGÀY SINH CHO SINH VIÊN:')
        update_student_birth_date(students)
    if menu == 26:
        print('CẬP NHẬT SỐ TÍN CHO MÔN HỌC: ')
        update_credit_subject(subjects)
    if menu == 27:
        print('CẬP NHẬT ĐỊA CHỈ CHO SINH VIÊN: ')
        update_student_address(students)
    if menu == 28:
        print('THAY ĐỔI MÔN HỌC CHO SINH VIÊN TRONG BÀNG ĐĂNG KÝ')
        update_subject_register(registers,subjects)
    if menu == 29:
        print('XÓA MÔN HỌC THEO MÃ MÔN HỌC:')
        delete_subject(subjects,registers)
    if menu == 30:
        print('XÓA BẢN ĐĂNG KÝ THEO MÃ SINH VIÊN VÀ MÃ MÔN HỌC: ')
        delete_register(registers)
    if menu == 31:
        print('XÓA TẤT CẢ SINH VIÊN CÓ HỌ: ')
        delete_student_by_last_name(students,registers)

