# Write your code here
# https://workat.tech/problem-solving/practice/add-one
try:
	name,age = input().split(' ')
	print('Hello '+name+'! Next year, you will be '+str(int(age)+1)+' years old')
except:EOFError