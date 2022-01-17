# Write your code here
# https://workat.tech/problem-solving/practice/print-digits
try:
	t = int(input())
	while t:
		# s = input()
		# print(s[0],s[1])
		n = int(input())
		print(n//10,n%10)
		t-=1
except:EOFError