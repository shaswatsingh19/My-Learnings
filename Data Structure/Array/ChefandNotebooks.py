# problem :https://www.codechef.com/problems/CNOTE

try:
    t = int(input())
    while t:
    	'''
    	x = poem page,y =left wewant= x-y
    	k = remaining cost , n=list
    	'''
    	f = 0
    	x,y,k,n= map(int,input().split())
    	pc =[]
    	for i in range(n):
    		p,c= map(int,input().split())
    		if p>=(x-y) and c<=k:
    			f = 1
    	if f==1:
    		print('LuckyChef')
    	else:
    		print('UnluckyChef')
    	t-=1
except:
    EOFError

'''
Sample
Input
3
3 1 2 2
3 4
2 2    
3 1 2 2
2 3
2 3    
3 1 2 2
1 1
1 2

Output
LuckyChef
UnluckyChef
UnluckyChef
'''