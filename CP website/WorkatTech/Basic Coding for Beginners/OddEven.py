# Write your code here
# https://workat.tech/problem-solving/practice/odd-even
try:
	t = int(input())
	while(t):
		n = int(input())
		if(n%2):print('ODD')
		else:print('EVEN')
		t-=1
except:EOFError