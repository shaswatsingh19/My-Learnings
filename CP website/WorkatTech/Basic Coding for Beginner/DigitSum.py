# Write your code here
try:
	t= int(input())
	while(t):
		n = int(input())
		s=0
		while(n>0):
			s += n%10
			n = n//10
		print(s)
		t-=1
except:
	EOFError