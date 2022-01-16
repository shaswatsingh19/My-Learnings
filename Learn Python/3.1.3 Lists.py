'''
List are used to store other value
might contain different data types value 
'''

square  = [1,4,9,16]

print(type(square)) # <class 'list'>

print(square[0]) # 1
print(square[-1]) # 16
print(square[2:4]) # 9 16


square = square + [25,36,49,64]
print(square)

square[0] = -1 # mutable can be changed
print(square) # [-1, 4, 9, 16, 25, 36, 49, 64]


square.append(81) # adding to the end of list
print(square) # [-1, 4, 9, 16, 25, 36, 49, 64, 81]


letter =['a', 'b', 'c', 'd', 'e', 'f', 'g']

letter[1:3] = ["B","C"]
print(letter) # ['a', 'B', 'C', 'd', 'e', 'f', 'g']


print("Length of square list is ",len(square) )

a = [
        [0,1,2],
        ['a','b','c'] ]
print(a[0]) # [0,1,2]
print(a[1][2]) # c
