'''
Sort an array of 0s, 1s and 2s without sorting
Algorithm:
We are using three pointer or variable low,mid,high
low and mid point to start and high point to end
Cases:
1.If arr[mid]==0 that is it should be infront of array
So we swap swap(arr[mid],arr[low]) with incrementing low and mid value by 1
2.If arr[mid]==1 then we doesn't want any thing we just simply increment mid + 1
as we know we got the middle value as 1
3.if arr[mid] == 2 then we swap(arr[mid],arr[high]) and decrement the high pointer by 1

'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


t = int(input())
while t:
	n = int(input())
	arr = list(map(int,input().split()))
	l = 0
	m = 0
	h = n-1
	while m<=h:
		if arr[m]==0:
			arr[m],arr[l]= arr[l],arr[m]
			l+=1
			m+=1
		elif arr[m]==1:
			m+=1
		else:
			arr[h],arr[m]= arr[m],arr[h]
			h-=1
	print(arr)
	t-=1

'''
It take O(n) time and O(1) space
Input:
2
5
0 1 2 1 0 
6
2 1 0 0 1 2
Output:
[0, 0, 1, 1, 2]
[0, 0, 1, 1, 2, 2]

'''
