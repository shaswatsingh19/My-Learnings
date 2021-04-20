# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


n,m= input().split()
n = int(n)
m = int(m)
mat =[]
for i in range(n):
	a = list(map(int,input().split()))
	mat.append(a)
x = int(input())
f = 0
for i in range(n):
	for j in range(m):
		if x == mat[i][j]:
			f = 1
if f==0:
	print('will take number')
else:
	print('will not take number')


'''

Input
2 2
1 2
3 4
3
Participant's output
will not take number
Checker comment
ok single line: 'will not take number'


Input
2 2
1 2
3 4
10
Participant's output
will take number
Checker comment
ok single line: 'will take number'
'''