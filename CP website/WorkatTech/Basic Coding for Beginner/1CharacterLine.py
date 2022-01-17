# Write your code here
try:
	name ,dob  = input().split(' ')
	print('Happy Birthday '+name+'! Your current age is '+str(2020-int(dob)))
except:EOFError