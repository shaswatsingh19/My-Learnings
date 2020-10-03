#  https://www.codechef.com/MAY20B/problems/CORUS

def query(c,s):
    d = {}
    for i in s:
        if i not in d:
            d[i] = 1
        elif d[i] != c:
            d[i] = d[i] + 1
    add = sum(d.values())
    return add
    
            


t = int(input())
while t:
    n,q = input().split()
    n = int(n)
    q = int(q)
    string = input()
    for i in range(q):
        center  = int(input())
        value = query(center,string)
        diff = n - value
        print(diff)
        
    
    t = t -1
