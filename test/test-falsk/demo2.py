# def generate_pairs(m: int, n: int):
#     list_a = []
#     for i in range(m,n + 1):
#         for j in range(m,n+1):
#             if i <= j:
#                 list_a.append((i,j))
#
#     return list_a
# print(generate_pairs(1,3))
#
# assert generate_pairs(2, 4) == [(2, 2), (2, 3), (2, 4), (3, 3), (3, 4), (4, 4)]
#
# a = "123456"
# print(a[-1::])
# s = " 你好中国 "
# print(" ".join(s.split()))

l = [[1, 2], [3, 4], [5, 6]]
x = [j for i in l for j in i]
print(x)
import random
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print(a)
