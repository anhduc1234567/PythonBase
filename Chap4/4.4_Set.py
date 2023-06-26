''' Lọc phần tử chỉ xuất hiêện 1 lần'''
# n = [x for x in input().split()]
# set = set()
# for i in n:
#     if i not in set:
#         set.add(i)
# print(set)
'''tìm các từ xuất hiện trong cae 2 chuỗi'''
def max_len(arr):
    max = 0
    for i in arr:
        if len(i) > max:
            max = len(i)
    return max

s1 = {x for x in input().split()}
s2 = {x for x in input(). split()}
s3 = s1.intersection(s2) # chung của cacr 2 chuoi
s4 = s1.symmetric_difference(s2)
print(f"Chuỗi chung của s1 và s2 {s3}")
print(f"Chỉ xuat hien ở s1 hoặc s2 {s4}")
