Problem :-https://codeforces.com/problemset/problem/122/A

Solution :-
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

arr = [47, 74, 447, 474, 477, 744, 747, 774,4,7]
n = int(input())
f = 1
if n in arr:
	f = 0
	print('YES')
else:
	for i in arr:
		if n%i==0:
			f = 0
			print('YES')
			break

if f:print('NO')
