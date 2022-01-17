# Write your code here
# https://workat.tech/problem-solving/practice/n-factorial
def fact(n):
	if n<2:return 1
	return n*fact(n-1)


try:
	t = int(input())
	while(t):
		n = int(input())
		ans = fact(n)
		print(ans)
		t-=1
	
except:
	EOFError