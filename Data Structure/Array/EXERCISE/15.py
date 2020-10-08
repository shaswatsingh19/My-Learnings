# Write a Python program to flatten a shallow list.

from itertools import chain
# we are going to make new list with all the merged elements
lst = [[1,2],[3,4,5],[6,7],[8,9,10]]

flatted_list = list(chain(*lst))

print(flatted_list)