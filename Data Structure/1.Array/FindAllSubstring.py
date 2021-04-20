'''
Program to print all the substring of the given string
Substring :- sequence of string in contiguous form
'''
import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


t  =int(input())
while t:
	n = int(input())
	arr =input()
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
abcd
3
xyz
 
Output:
a
ab
abc
abcd
b
bc
bcd
c
cd
d

x
xy
xyz
y
yz
z

'''
