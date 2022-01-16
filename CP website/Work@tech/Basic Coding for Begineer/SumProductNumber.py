# https://workat.tech/problem-solving/practice/sum-product-number
# Write your code here
try:
	t= int(input())
	while(t):
		n = int(input())
		temp = n
		s=0
		p=1
		while(n>0):
			r = n%10
			s+=r
			p*=r
			n = n//10
		if(p*s != temp):print('No')
		else:print('Yes')
		t-=1
except:
	EOFError