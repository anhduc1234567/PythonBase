while True:
    try:
        i = int(input('Nhap thu: '))
        if int(i) == 0:
            break
        if int(i) < 1 or int(i) >7:
            raise ValueError('Loi nhap lại')
        print("Correct")
    except ValueError as e:
        print(e)
