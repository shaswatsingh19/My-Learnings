# Write a Python program to sum all the items in a list


li = [1,2,3,4,5,6]
# the below line take the input in one line
li1 = list(map(int,input().split()))
result = sum(li)
result1 = sum(li1)
print('Sum of all element of  li is',result)
print('Sum of all element of li1 is ', result1)



'''
I/O:-

4 1 5 9 10
Sum of all element of  li is 21
Sum of all element of li1 is  29

'''
