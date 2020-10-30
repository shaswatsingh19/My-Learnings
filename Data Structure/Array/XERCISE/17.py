# Write a Python program to select an item randomly from a list.

import random

lst = [1, 2, 3, 4, 'one', 'two', 'three', 'four']

idx = random.randint(0,len(lst)-1)
print('the index is',idx)
print('the item is',lst[idx])  
'''
Output :-
the index is 0
the item is 1

the index is 4
the item is one

the index is 3
the item is 4

'''  