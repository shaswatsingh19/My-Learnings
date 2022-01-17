# Write your code here
# https://workat.tech/problem-solving/practice/divisible-by-six
try:
	t = int(input())
	while(t):
		n  = int(input())
		if(n%6):print(False)
		else:print(True)
		t-=1
except:EOFError