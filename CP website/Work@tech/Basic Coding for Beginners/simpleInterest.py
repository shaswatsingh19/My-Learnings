# https://workat.tech/problem-solving/practice/simple-interest
# Write your code here
try:
	p,r,t = input().split(' ')
	p = float(p)
	r = float(r)
	t = float(t)
	ans =(p*r*t)/100
	print("%.6f"%ans)
except:EOFError