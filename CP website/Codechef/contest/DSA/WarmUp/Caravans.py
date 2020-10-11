# https://www.codechef.com/LRNDSA01/problems/CARVANS

t = int(input())

for i in range(t):
    n = int(input())
    c = list(map(int,input().split()))
    count = 1
    for i in range(1,n-1):
        if c[i] < c[0]:
            if c[i+1] < c[i]:
                count - count + 1
        
    
