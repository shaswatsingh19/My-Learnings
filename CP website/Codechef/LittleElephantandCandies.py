# Problem : https://www.codechef.com/problems/LECANDY

try:
    t = int(input())
    while t:
    	f = 1
    	n,c= map(int,input().split())
    	arr = list(map(int,input().split()))
    	for i in range(n):
    		c = c - arr[i]
    		if c<0:
    			f=0
    			print('No')
    			break
    	if f:
    		print('Yes')
    	t-=1
except:
    EOFError

'''
Example
Input:
2
2 3
1 1
3 7
4 2 2

Output:
Yes
No

'''
