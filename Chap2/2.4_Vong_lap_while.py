'''Tìm ước chung và bội chung'''
import math

# str_a, str_b = (input()).split()
# a = int(str_a)
# b = int(str_b)
# c = 0
# d = 0
# if a < b:
#     c = a
#     d = b
# else:
#     c = b
#     d = a
# while c > 0:
#     if a % c == 0 and b % c == 0:
#         print(c, end=" ")
#         c = -1
#     c -= 1
#
# while d > 0:
#     if d % a == 0 and d % b == 0:
#         print(d)
#         d = -1
#     d += 1
'''Tổng binhg ohuowng các chữ số'''
# n = int(input())
# sum = 0
# while n > 0:
#     sum = sum + ((n%10) ** 2)
#     n = n // 10
#
# print(sum)
'''Phân tích thừa số nguyên tố'''
# n = int(input())
# i = 2
# c = 0
# while n != 1:
#     if n % i == 0:
#         c += 1
#         n = n // i
#     else:
#         if c > 0:
#             print(i, end=" ")
#             if c > 1:
#                 print("^",c, end="")
#             if i != n // i:
#                 print("x",end="")
#         i += 1
#         c = 0
#
# print(i, end="")
# if c > 1:
#     print("^",c)
'''Tính n!'''
# n = int(input())
# giai_thua = 1
# while n != 1:
#     giai_thua = giai_thua * n
#     n -= 1
# print(giai_thua)
'''Số nguyên tố cùng nhau'''
# str_a, str_b = (input()).split()
# a = int(str_a)
# b = int(str_b)
# c = 0
# d = 0
# if a <0  or b <= 0: print("INVALID")
# else :
#     if a < b:
#         c = a
#         d = b
#     else:
#         c = b
#         d = a
#     while c > 0:
#         if a % c == 0 and b % c == 0:
#             if c != 1 :
#                 print("NO")
#             else:
#                 print("Yes")
#             c = -1
#         c -= 1
''' Tính tổng 1/k ** 3 k chạy từ 1 đến n'''
# n = int(input())
# sum = 0
# k = 1
# while k != n+1:
#     sum = sum + (1/(k**3))
#     k += 1
# print(sum)
'''Nhap so nguyen in ra tháng'''
# menu = 1
# while menu != 0:
#     print("Nhap tháng 1- 12")
#     print("Nhap 0 to exit")
#     menu = int(input())
#     if menu != 0:
#         match menu:
#             case 1:
#                 print("January")
#             case 2:
#                 print("February")
#             case 3:
#                 print("March")
#             case 4:
#                 print("April")
#             case 5:
#                 print("May")
#             case 6:
#                 print("June")
#             case 7:
#                 print("July")
#             case 8:
#                 print("August")
#             case 9:
#                 print("September")
#             case 10:
#                 print("October")
#             case 11:
#                 print("November")
#             case 12:
#                 print("December")
#             case _:
#                 print("INVALID")
#     else:
#         print("Thoat chuong trình ")
#     print("===================================")
'''Tính cung hoàng đạo'''
menu = 1
while menu != 0:
    print("Nhap 0 to exit")
    print("Nhap số khác khoong để tiếp tục")
    menu = int(input())
    if menu != 0:
        str_day, str_month = input("Nhap ngày tháng :").split()
        day = int(str_day)
        month = int(str_month)
        match month:
            case 1:
                if day >= 1 and day <= 19:
                    print("Ma Kết")
                elif day >= 19 and day <= 31:
                    print("Bảo Bình")
                else:
                    print("Invalid day")
            case 2:
                if day >= 1 and day <= 18:
                    print("Bảo Bình")
                elif day >= 19 and day <= 29:
                    print("Song Ngư")
                else:
                    print("Invalid day")
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
        print("==================")
print("THANKS")

