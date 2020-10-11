Problem :- https://www.codechef.com/CZEN2020/problems/ZRACE

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')

try:
    
    t = int(input())
    while t:
    	arr = list(map(int,input().split()))
    	if arr[0] >= max(arr):
    		print('Champions')
    	else:
    		print(-1)
    	t -=1
except:
    EOFError
