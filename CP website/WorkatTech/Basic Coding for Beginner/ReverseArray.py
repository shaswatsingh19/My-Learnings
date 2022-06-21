# Write your code here
# https://workat.tech/problem-solving/practice/toggle-case
# Write your code here
try:
	t = int(input())
	arr = list(input().split())
	i = 0;
	j = len(arr)-1
	while(i<j):
		arr[i],arr[j] = arr[j],arr[i]
		i+=1
		j-=1
	print(" ".join(arr))
	
except:EOFError