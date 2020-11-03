#code
# Problem : https://practice.geeksforgeeks.org/problems/union-of-two-arrays/0#

t = int(input())
while t:
	a,b=map(int,input().split())
	arr = list(map(int,input().split()))
	brr = list(map(int,input().split()))
	arr=set(arr)
	brr=set(brr)
	print(len(arr.union(brr)))
	t-=1

'''
Example:
Input:
2
5 3
1 2 3 4 5
1 2 3
6 2
85 25 1 32 54 6
85 2
Output:
5
7
'''