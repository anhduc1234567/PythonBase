def check_gpa():
    try:
        gpa = input('Nhap diem trung binh: ')
        gpa = float(gpa)
        if gpa < 0.0 or gpa > 4.0:
            raise ValueError('Loi')
        else:
            return gpa
    except ValueError as e:
        raise RuntimeError('khong the phan loai ') from e


try:
    gpa = check_gpa()
    print(gpa)
except RuntimeError as e:
    print(e)