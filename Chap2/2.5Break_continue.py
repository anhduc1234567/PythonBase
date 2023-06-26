import math
stra, strb, strk = input().split()
a = int(stra)
b = int(strb)
k = int(strk)
if a < 0 or b < 0 or a > b or k <= 0:
    print("NOT AVAILABLE")
else:
    count = 0
    for i in range(a, b + 1,1):
        isPrime = True
        bound = int(math.sqrt(i))
        for j in range(2,bound + 1,1):
            if i % j == 0:
                isPrime = False
                break
        if isPrime and count < k:
            print(i, end=" ")
            count += 1
        elif count >= k:
            break

