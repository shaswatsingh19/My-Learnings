# Write your code here
# https://workat.tech/problem-solving/practice/square-sum
try:
	t = int(input())
	while(t):
		n = int(input())
		s = 0
		while(n>0):
			r = n%10
			s += r*r
			n = n//10
		
		print(s)
		t-=1
except:EOFError