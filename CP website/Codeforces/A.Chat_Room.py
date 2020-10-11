PROBLEM :- https://codeforces.com/contest/58/problem/A
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

s = input()
ori  = 'hello'
j = pas = 0
for i in range(len(s)):
	if s[i] == ori[j]:
		j += 1
		pas += 1

		if pas == 5:
			break

if pas == 5:
	print('YES')
else:
	print('NO')
