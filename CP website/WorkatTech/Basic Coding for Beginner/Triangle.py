# Write your code here
# https://workat.tech/problem-solving/practice/triangle
try:
	t = int(input())
	while t:
		arr = list(map(int,input().split(' ')))
		m = max(arr)
		index = arr.index(m)
		arr.pop(index)
		if(sum(arr)>=m):print(sum(arr)+m)
		else:print(-1)
		t-=1
except:EOFError