'''
Move all the negative elements to one side of the array 
'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


t = int(input())
while t:
	arr = list(map(int,input().split()))
	n =len(arr)
	l=0
	m=0
	h=n-1
	while m<=h:
		if arr[m]<0:
			arr[m],arr[l]=arr[l],arr[m]
			l+=1
			m+=1
		elif arr[m]>=0:
			arr[m],arr[h]=arr[h],arr[m]
			h-=1
	print(arr)
	t-=1

'''
It take O(n) time and O(1) space
Input:
3
32 -323 1 12 -54 0 323 -9
32 -3 133 4 0 -3 19
1 1 12 -54 -101 323 -93

Output:
[-9, -323, -54, 12, 0, 323, 1, 32]
[-3, -3, 4, 0, 133, 19, 32]
[-93, -101, -54, 12, 323, 1, 1]


'''
