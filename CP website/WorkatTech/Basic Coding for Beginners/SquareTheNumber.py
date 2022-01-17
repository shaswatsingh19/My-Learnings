# https://workat.tech/problem-solving/practice/square-the-number
try:
	t = int(input())
	while(t):
		n = int(input())
		print(n*n)
		
		t-=1
		
except:
	EOFError