# Problem :- https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/

# Solution :-

import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')


arr = list(map(int,input().split()))

maxi = -999999999
mini = 9999999999

for i in arr:
	if i>maxi:
		maxi = i
	elif i<mini:
		mini = i 
print(maxi,mini)
