# https://workat.tech/problem-solving/practice/armstrong-number
# Write your code here
try:
	t= int(input())
	while(t):
		n = int(input())
		temp = n
		s=0
		while(n>0):
			r = n%10
			s += r*r*r
			n = n//10
		if(temp!=s):print('No')
		else:print('Yes')
		t-=1
except:
	EOFError