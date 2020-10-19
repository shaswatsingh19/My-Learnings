problem :- https://codeforces.com/problemset/problem/41/A

Solution :-

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


a = input()
b = input()

a = list(a)
b = list(b)
new = []
for i in range(len(a)-1,-1,-1):
	new.append(a[i])

if b == new:
	print("YES")
else:
	print("NO")
