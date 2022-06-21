# https://workat.tech/problem-solving/practice/win-or-lose
try:
	n = int(input())
	arr  = list(map(int,input().split(' ')))
	if(max(arr)%2==0):print('WON')
	else:print('LOST')
except:EOFError