import math
# giải phương trình bac nhất
# a = int(input("Nhâp số a "))
# b = int(input("Nhấp số b "))
# if a != 0 :
#     print("Phương trình có 1 nghiệm duy nhất: x = ", -b/a)
# elif a == 0 and b == 0:
#     print("Phuong trinh vô số nghiệm")
# elif a == 0 and b != 0:
#     print("Phương trình vô nghiệm")
# giải phương trình bậc 2
str_a , str_b, str_c =input("Nhập 3 số a, b, c: ").split()
a = int(str_a)
b = int(str_b)
c = int(str_c)

if a == 0:
    if b != 0:print("Phương trình có nghiệm duy nhất ", -c/b)
    if b == 0:
       if c == 0:print("Phương trình vô số nghiệm")
       else :print("Phương trình vô nghiệm")
else:
    denta = (b ** 2) - (4 * a * c)
    if denta == 0:
        print("Phương trình có 1 nnghiemeh duy nhất x = ", -b/(2*a))
    elif denta > 0:
        print("Phương trình có 2 nghiệm : ")
        print("x1 = ", (-b + math.sqrt(denta)) / (2 * a))
        print("x2 = ", (-b - math.sqrt(denta)) / (2 * a))
    else:
        print("Phương trình vô nghiệm")
# check 3 số 3 a b c có tạp thành tam giác không
if a < (b + c) and a > abs(b - c):
    print("có la tam giác")
else : print("Khong la tam giác")

# check xem có phải tam giác vuông không
a_2 = a * a
b_2 = b * b
c_2 = c * c
if a_2 == b_2 + c_2 or b_2 == a_2 + c_2 or c_2 == a_2 + b_2:
    print("CÓ VUÔNG ")
else:
    print("No")



