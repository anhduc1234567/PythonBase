n = int(input("Nhap so n "))
match n:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("INVALID")
str_day,str_month = input("Nhap ngày tháng ").split()
day = int(str_day)
month = int(str_month)

match month:
    case 1:
        if day >=1 and day <=19 :
            print("Ma Kết")
        elif day >=19 and day <=31:
            print("Bảo Bình")
        else: print("Invalid day")
    case 2:
        if day >= 1 and day <= 18:
            print("Bảo Bình")
        elif day >= 19 and day <=29:
            print("Song Ngư")
        else: print("Invalid day")
    case 3:
        if day >= 1 and day <= 20:
            print("Song Ngư")
        elif day >= 21 and day <= 31:
            print("Bạch Dương")
        else:
            print("Invalid day")
    case 4:
        if day >= 1 and day <= 20:
            print("Bạch Dương")
        elif day >= 21 and day <= 30:
            print("Kinh Ngưu")
        else:
            print("Invalid day")
    case 5:
        if day >= 1 and day <= 20:
            print("Kim Ngưu")
        elif day >= 21 and day <= 31:
            print("Song Tử")
        else:
            print("Invalid day")
    case 6:
        if day >= 1 and day <= 21:
            print("Song Tử")
        elif day >= 22 and day <= 30:
            print("Cự Giải")
        else:
            print("Invalid day")
    case 7:
        if day >= 1 and day <= 22:
            print("Cự Giải")
        elif day >= 23 and day <= 31:
            print("Sư Tử")
        else:
            print("Invalid day")
    case 8:
        if day >= 1 and day <= 22:
            print("Sư tử")
        elif day >= 23 and day <= 31:
            print("Xử Nữ")
        else:
            print("Invalid day")
    case 9:
        if day >= 1 and day <= 22:
            print("Xử Nữ")
        elif day >= 23 and day <= 30:
            print("Thiên Bình")
        else:
            print("Invalid day")
    case 10:
        if day >= 1 and day <= 23:
            print("Thiên Bình")
        elif day >= 24 and day <= 31:
            print("Bọ Cạp")
        else:
            print("Invalid day")
    case 11:
        if day >= 1 and day <= 22:
            print("Bọ Cạp")
        elif day >= 23 and day <= 30:
            print("Nhân Mã")
        else:
            print("Invalid day")
    case 12:
        if day >= 1 and day <= 21:
            print("Nhân Mã")
        elif day >= 22 and day <= 31:
            print("Ma Kết")
        else:
            print("Invalid day")