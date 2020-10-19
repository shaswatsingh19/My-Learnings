# Problem Statement:- https://codeforces.com/problemset/problem/116/A


# Solution :- 
# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


n = int(input())
current = 0
max_curr = 0
while n:
	exit,enter = map(int,input().split())
	current = current - exit + enter
	if current > max_curr:
		max_curr = current

	n-=1
print(max_curr)
