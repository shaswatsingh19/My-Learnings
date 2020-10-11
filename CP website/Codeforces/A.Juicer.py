Problem :- https://codeforces.com/contest/709/problem/A

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


n,b,d = map(int,input().split())
c = 0
juice = 0
arr = list(map(int,input().split()))
for  i in arr:
	if i <= b:
		juice += i
		if juice > d:
			c +=1
			juice = 0
print(c)
