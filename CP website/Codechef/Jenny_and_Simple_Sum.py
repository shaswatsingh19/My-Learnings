Problem :- https://www.codechef.com/CZEN2020/problems/SIPM

# import sys
# sys.stdin = open('input.txt','r')
# sys.stdout = open('output.txt','w')


try:
    t = int(input())
    while t:
    	pos = []
    	neg = []
    	n = int(input())
    	arr = list(map(int,input().split()))
    	for i in arr:
    		if i > 0 :
    			if i not in pos:
    				pos.append(i)
    		elif i <0:
    			if i not in neg:
    				neg.append(i)
    	print(sum(pos),sum(neg))
    
    	t -=1
except:
    EOFError
