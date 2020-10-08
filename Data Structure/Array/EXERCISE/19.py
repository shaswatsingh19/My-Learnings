# Write a Python program to generate all permutations of a list in Python.
from itertools import permutations

lst = [11,22,33]
all_lst = permutations(lst)
for i in all_lst:
    print(i)

'''
Output:-

(11, 22, 33)
(11, 33, 22)
(22, 11, 33)
(22, 33, 11)
(33, 11, 22)
(33, 22, 11)

'''