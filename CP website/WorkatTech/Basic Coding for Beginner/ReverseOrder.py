# Write your code here
try:
	n = int(input())
	arr = list(map(int,input().split()))
	arr.reverse()
	ans = ''
	for i in arr:
		ans += str(i)+" "
	print(ans.rstrip()) # rstrip() remove the last space from string
except:EOFError