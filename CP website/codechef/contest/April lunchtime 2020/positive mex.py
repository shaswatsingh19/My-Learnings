# https://www.codechef.com/LTIME83B/problems/MEXUM

from itertools import chain , combinations

def ps(iterable):
	s = list(iterable)
	return chain.from_iterable(combinations(s,r) for r in range(len(s) +1))

def mex(n):
    a = input().split()
    a  = "".join(a)
    a  = list(ps(a))
    add = 1
    for i in range(1,len(a)):
        for j in range(1,1000):
            if str(j) not in a[i]:
                add = add + j
                break
    return add        
    
    

t = int(input())
while t:
    n = int(input())
    print(mex(n))
    t = t -1
