'''
Permutation with arrays
# 
'''

import sys
sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

#code
# method 1 - Brute force



def bin(n,l,h):
	m = (l +  h) / 2
	while l<h:
	    mult = '%.3f'%(m*m)
	    mult = float(mult)
	    if mult == n:
	        return m
	    elif mult<(n):
	        l = m
	        return bin(n,l,h)
	    else:
	        h = m 
	        return bin(n,l,h)
	return  m
n = int(input())
flag = 0
for  i in range(1,n):
	if i*i == n:
		print(i)
		flag = 1
		break

i=1
if flag==0:
	while i*i<=n:
		i+=1
	low = i-1
	high = i
	ans = bin(n,low,high)
	print(ans)

