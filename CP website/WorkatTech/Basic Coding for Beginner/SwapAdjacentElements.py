# https://workat.tech/problem-solving/practice/swap-adjacent
# Write your code here
try:
	n  = int(input())
	arr = list(map(int,input().split()))
	if(n%2!=0):n=n-1
	for i in range(0,n,2):
		arr[i],arr[i+1] = arr[i+1],arr[i]
	s = ''
	for i in arr:
		s += str(i)+" "
	print(s)
except:EOFError