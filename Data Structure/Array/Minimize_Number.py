'''
Given a number N and an array A of N positive numbers. Print maximum possible operations that can be performed.

The operation is as follows: if all numbers are even then divide each of them by 2 otherwise, you can not perform any more operations.

Input
First line contains a number N (1 ≤ N ≤ 200) number of elements.

Second line contains N numbers (1  ≤  Ai  ≤  109).

Output
Print the maximum possible number of operations that can be performed.

'''
c=0
f=1
t = int(input())
arr = list(map(int,input().split()))
while 1:
	for i in range(t):
		if arr[i]%2==0:
			arr[i]=arr[i]//2
		else:f=0
	if f==0:
		break
	c+=1
	print(arr)
print(c)

'''

input:
3
8 12 40
output:
2

input:
4
5 6 8 10
output:
0
'''