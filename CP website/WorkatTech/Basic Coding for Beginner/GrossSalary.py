# Write your code here
# https://workat.tech/problem-solving/practice/gross-salary
try:
	t  = int(input())
	l = list(map(int,input().split()))
	h = l[0]
	d = l[1]
	b = l[2]
	while(t):
		sal = int(input())
		sal = sal/100
		gross = sal*100 + (sal*h)+(sal*d)+(sal*b)
		print(format(gross,".2f"))
		t-=1
except:EOFError