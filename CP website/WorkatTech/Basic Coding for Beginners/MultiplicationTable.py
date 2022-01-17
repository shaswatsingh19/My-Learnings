# Write your code here
# https://workat.tech/problem-solving/practice/multiplication-table
try:
	t = int(input())
	while(t):
		n = int(input())
		s = ''
		for i in range(1,11,1):
			s += str(i*n)+" "
		# s.rstrip()
		print(s)
		t-=1
except:
	EOFError