# Write your co
# de here
# https://workat.tech/problem-solving/practice/pastries
try:
	p,q = input().split(" ")
	p = int(p)
	q = int(q)
	while(q):
		c = int(input())
		if(p>0):
			print('Enjoy your dessert!')
			p = p - c
		else:
			print('Sorry, we are all out!')
		q-=1
except:EOFError