a = int(input("Nhap so a : "))

if a % 2 == 0 : print("EVEN")
else: print("ODD")

if a > 0 :
    print("Positive")
elif a < 0 :
    print("Negative")
else:
    print("Unsigned")

b = int(input("Nhap so b : "))

if a == b :
    print("equal")
elif a > b:
    print("Different ", a - b)
else :
    print("Different ", b - a)

# tim so lớn nhất

c = int(input("Nhap so c: "))
if a ==b and b == c : print("No result")
elif a >= b and a >= c : print("a la so lớn nhất")
elif b >= a and b >= c: print("b la so lớn nhất")
elif c >= a and c >= b: print("c là số lớn nhất")

