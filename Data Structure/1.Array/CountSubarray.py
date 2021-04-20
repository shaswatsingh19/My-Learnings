'''
Count Subarrays
Given a number N and an array A of N numbers. Print the number of sub-arrays which are non-decreasing.
arr = [1 ,4 ,2]
output =>
[1],[4],[2],[1,4] 
so ouput would be 4
'''

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

#code
# method 1 - Brute force
t = int(input())
while t:
	n = int(input())
	c = 0
	arr = list(map(int,input().split()))
	for i in range(n+1):
		for j in range(i+1,n+1):
			ran = arr[i:j]
			if len(ran)==1:
				c+=1
				continue
			elif ran == sorted(ran):
				c+=1
			
	print(c)
	t-=1



'''

'''
