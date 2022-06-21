# Write your code here
# https://workat.tech/problem-solving/practice/number-reversal
try:
	n  = int(input())
	rev = 0
	while(n>0):
		r = n%10
		rev = rev*10 +  r
		n = n//10
	print(rev)
	
		
except:EOFError