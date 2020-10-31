'''
Program to print all the subarray of the given array
Subarray :- sequence of array in contiguous form
'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


t  =int(input())
while t:
	n = int(input())
	arr =list(map(int,input().split()))
	for i in range(n):
		for j in range(i,n):
			print(arr[i:j+1])
	print()
	t-=1

'''
We can find max of (n*n+1)/2 subarray from n element array
Input:
2
4
1 6 3 7

3
3 1 2
 
Output:
[1]
[1, 6]
[1, 6, 3]
[1, 6, 3, 7]
[6]
[6, 3]
[6, 3, 7]
[3]
[3, 7]
[7]

[3]
[3, 1]
[3, 1, 2]
[1]
[1, 2]
[2]


'''
