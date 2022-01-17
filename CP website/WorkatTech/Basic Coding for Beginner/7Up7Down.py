# Write your code here
# https://workat.tech/problem-solving/practice/7-up-7-down
try:
	t = int(input())
	while(t):
		n = int(input())
		if(n>7):print('UP')
		elif(n<7):print('DOWN')
		else:print('EQUAL')
		t-=1
except:EOFError