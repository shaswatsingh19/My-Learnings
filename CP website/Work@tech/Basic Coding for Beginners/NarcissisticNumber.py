# https://workat.tech/problem-solving/practice/narcissistic-number
# Write your code here
try:
	t = int(input())
	while(t):
		n = input()
		l = len(n)
		n = int(n)
		temp = n
		s = 0
		while(temp>0):
			r = temp%10
			s += pow(r,l)
			temp = temp//10
		if(s==n):print("Yes")
		else:print('No')
		t-=1
		
except:
	EOFError