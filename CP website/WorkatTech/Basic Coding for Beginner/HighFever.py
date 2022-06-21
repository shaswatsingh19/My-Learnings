# Write your code here
# https://workat.tech/problem-solving/practice/pastries
try:
	t = int(input())
	f = ''
	while(t):
		name , temp = input().split(' ')
		temp = float(temp)
		
		if(temp>98.6):
			f += name+", "
		t-=1
	print(f.rstrip(', '))
except:
	EOFError