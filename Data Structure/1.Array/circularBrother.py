'''
Write a python program to check whether two lists are circularly identical.

Circular identical means
lst = [1,2,3]
mst = [3,2,1] are circular identical
'''


l1 = [1,2,3]
l2 = [3,2,1]
l2.reverse()
if l1==l2:
    print('True')
else:
    print('False')
    