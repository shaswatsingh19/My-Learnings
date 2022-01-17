# Write your code here
# https://workat.tech/problem-solving/practice/milkman

try:
	r,h = input().split(' ')
	r = float(r)
	h = float(h)
	v  = (3.14* r*r*h)/1000
	p = v*40
	print("%.2f"%p)
except:EOFError