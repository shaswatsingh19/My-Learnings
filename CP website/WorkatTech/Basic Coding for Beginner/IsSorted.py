# https://workat.tech/problem-solving/practice/is-sorted
# Write your code here
try:
	t = int(input())
	while(t):
		n = int(input())
		arr = list(map(int,input().split()))
		check = 'Yes'
		for i in range(n-1):
			if(arr[i]>arr[i+1]):
				check='No'
				break;
		print(check)
		t-=1
except:EOFError