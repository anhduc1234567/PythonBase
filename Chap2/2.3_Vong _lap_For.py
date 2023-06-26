# t = int(input())
# for j in range(1,t+1,1):
#     n = int(input())
#     if n >= 0:
#         sum = 0
#         for i in range(1,n + 1,1):
#             giaithua = 1
#             for x in range(1,i+1,1):
#                 giaithua = giaithua * x
#             sum = sum + giaithua;
#
#         print(f"Test {j}:")
#         print("{0:.3f}".format(sum))
#     else:
#         print(f"Test {j}:")
#         print("No result")
''' bài 7'''
# t =int(input())
# for i in range(1, t+1,1):
#     str_n, str_t = input().split()
#     n = int(str_n)
#     k = int(str_t)
#     print(f"Test {i}:")
#     if n < 0 or k <= 0: print("invalid")
#     else:
#         for j in range(1,n+1,1):
#             if j % k == 0:
#                 print(j, " ", end="")
''' bài 8 check số nguyên tố'''
# n = int(input())
# cout = 0
# if n < 2:
#     print("No")
# else:
#     for i in range(2,n,1):
#         if n % i == 0:
#             cout +=1
#     if cout == 0 :
#         print("Yes")
#     else:
#         print("No")
'''Bai 9 so thuan nghich'''
# n = abs(int(input()))
# k = n
# m = ""
# sum = 0
# tic = 1
# while n > 0 :
#     m = m + str(n%10)
#     sum  = sum + n%10
#     tic = tic*(n%10)
#     n = n // 10
#
# if int(m) == k:
#     print("yes")
# else: print("no")
#
# print("Tong cac chu so la ", sum)
# print("Tich cac chu so la ", tic)
'''Bài 12 tính số fibonacci'''
# n = int(input())
# f0 = 0
# f1 = 1
# fn = 1
# for i in range(1,n,1):
#     fn = f0 + f1
#     f0 = f1
#     f1 = fn
# print(fn)
''' Tìm các ước của n'''
# n = int(input())
#
# for i in range(1,n+1, 1):
#     if n % i == 0:
#         print(i, " ",end="")
'''vec hình chữ nhất 16'''
m = int(input())
for i in range(1,m+1,1):
    for j in range(0,i,1):
        print("* ", end="")
    print()
''' vẽ tam giac cân'''
h = int(input())
for i in range(1, h + 1,1):
    for j in range(1, 2 * h ,1):
        if h - i + 1 <= j <= h + i -1:
            print(" * ", end="")
        else:
            print("   ",end="")
    print()

for i in range(1, h + 1,1):
    for j in range(1, 2 * h ,1):
        if h - i + 1 <= j <= h + i -1:
            print(f" {i - abs(h - j)} ", end="")
        else:
            print("   ",end="")
    print()

for i in range(1, h + 1,1):
    for j in range(1, 2 * h ,1):
        if h - i + 1  == j or j== h + i -1 or i == h:
            print(f" 1 ", end="")
        else:
            print("   ",end="")
    print()
''' Vẽ trái tim 6 x 7'''
m = 6
n = 7
for i in range(1,m + 1,1):
    for j in range(1, n + 1, 1):
        if (i == 1 and j != 1 and j != 4 and j != 7) or \
                (i == 2 or i == 3) or \
                (i == 4 and j != 1 and j != 7) or \
                (i == 5  and (j == 3 or j == 4 or j ==5))or \
                (i == 6 and j == 4):
            print(" * ", end="")

        else:
            print("   ", end="")
    print()