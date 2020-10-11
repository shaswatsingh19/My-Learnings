
Problem :- https://codeforces.com/contest/294/problem/A


# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


n = int(input())
arr = list(map(int,input().split()))
m = int(input())
if n == 1 and m>0:
	print(0)
elif n == 1 and m == 0:
	print(arr[0])
else:
	for i in range(m):
		x,y = map(int,input().split())
		x -=1
		y -=1
		if x == 0:
			arr[x+1] = arr[x+1] + arr[x] - 1 - y
		elif x == n-1:
			arr[x-1] = arr[x-1] + y
		else:
			arr[x-1] = arr[x-1] + y
			arr[x+1] = arr[x+1] + arr[x] - 1 - y
		arr[x] = 0

	for i in arr:
		print(i)
