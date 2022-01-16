# Write your code here
# https://workat.tech/problem-solving/practice/not-divisible
try:
	t = int(input())
	while(t):
		n = int(input())
		s = ''
		for i in range(1,n+1,1):
			if(i%3!=0):
				s+= str(i)+" "
		print(s)
		t-=1
except:
	EOFError