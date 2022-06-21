# https://workat.tech/problem-solving/practice/max-in-matrix
# Write your code here
try:
	r,c=input().split(' ')
	r=int(r)
	c=int(c)
	mat = []
	m = -1
	for i in range(r):
		l = list(map(int,input().split(' ')))
		maxi  = max(l)
		if(maxi>m):
			m = maxi
		mat.append(l)
	print(m)
except:EOFError