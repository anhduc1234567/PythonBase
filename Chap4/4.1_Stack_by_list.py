def push(stack:list, value):
    stack.append(value)
def size(stack):
    return len(stack)
def is_empty(stack:list):
    return len(stack) == 0

def pop(stack :list):
    if(size(stack) == 0):
        return None
    else:
       return stack.pop()

def peek(stack:list):
    if is_empty(stack):
        return None
    return stack[size(stack) - 1]
'''đảo ngược chuỗi'''
# str = input("Nhap chuoi ")
# word = str.split()
# stack = []
# for i in word:
#     push(stack,i)
# for i in range(0,size(stack)):
#     print(pop(stack), end=" ")
'''check mảng đối xứng'''
# def check(stack, num):
#     i = 0
#     while is_empty(stack) is False:
#         if pop(stack) != num[i]:
#             return False
#         i += 1
#     return True
#
# n = int(input("Nhap so phan tử "))
# num = [int(y) for y in input().split()]
# stack = []
# for i in range(n//2,n,1):
#     push(stack,num[i])
# if check(stack,num):
#     print("YES")
# else:
#     print("No")
'''Trung tố Hậu tố'''
def priority(char):
    if char == "^":
        return 3
    elif char == "*" or char == "/":
        return 2
    elif char == "+" or char == "-":
        return 1
    return 0
def add_space(n:str):
    n = n.replace("*"," * ")
    n = n.replace("("," ( ")
    n = n.replace(")"," ) ")
    n = n.replace("^"," ^ ")
    n = n.replace("-"," - ")
    n = n.replace("+"," + ")
    n = n.replace("/"," / ")
    return n
def exchage(n,stack):
    for e in range(0, len(n), 1):
        if n[e] == "*" or n[e] == "+" or n[e] == "/" or n[e] == "-" or n[e] == "^":
            if is_empty(stack) is False:
                if priority(n[e]) <= priority(peek(stack)):
                    print(pop(stack), end=" ")
            push(stack, n[e])
        elif n[e] == "(":
            push(stack, n[e])
        elif n[e] == ")":
            op = pop(stack)
            while op != '(':
                print(op, end=" ")
                op = pop(stack)
        else:
            print(n[e], end=" ")
    while is_empty(stack) is False:
        print(pop(stack), end=" ")

# n = input("Nhap bieu thức : ")
# data = add_space(n).split()
# stack = []
# exchage(data,stack)

'''Tính giá trị biểu thức'''
# n = input("Nhap bieu thức : ")
# data = add_space(n).split()
# stack = []
# for i in data:
#     if priority(i) > 0 :
#         if i == "*":
#             a = int(pop(stack))
#             b = int(pop(stack))
#             push(stack, a * b)
#         elif i == "/":
#             a = int(pop(stack))
#             b = int(pop(stack))
#             push(stack, b / a)
#         elif i == "-":
#             a = int(pop(stack))
#             b = int(pop(stack))
#             push(stack, b - a)
#         elif i == "+":
#             a = int(pop(stack))
#             b = int(pop(stack))
#             push(stack, a + b)
#         elif i == "^":
#             a = int(pop(stack))
#             b = int(pop(stack))
#             push(stack, b ** a)
#     else:
#         push(stack,i)
# print(pop(stack))
'''sắp xêp tằng dần trong stack'''
# n = [int(x) for x in input().split()]
# stack = []
# for i in n:
#     if is_empty(stack) or i >= peek(stack):
#         push(stack,i)
#     else:
#         stack_tem = []
#         op = peek(stack)
#         while op is not None and i < op:
#             push(stack_tem,op)
#             pop(stack)
#             op = peek(stack)
#
#         push(stack, i)
#         while is_empty(stack_tem) is False:
#             push(stack, pop(stack_tem))
# for i in stack:
#     print(i, end=" ")
'''Trộn 2 stack đã sắp xếp tăng dần'''
def merger(m, n):
    result = []
    while is_empty(m) is False and is_empty(n) is False:
        if peek(m) > peek(n):
            push(result, peek(m))
            pop(m)
        else:
            push(result, peek(n))
            pop(n)
    while is_empty(m) is False:
        push(result, peek(m))
        pop(m)
    while is_empty(n) is False:
        push(result, peek(n))
        pop(n)
    return result

n = [int(x) for x in input().split()]
m = [int(y) for y in input().split()]
stack = merger(m,n)
for i in range(-1,-len(stack)-1,-1):
    print(stack[i], end=" ")
