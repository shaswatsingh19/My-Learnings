def chef (p,p_t,n,diff):
    for i in range(n):
        for j in range(i,n):
            if p_t[i] != p_t[j] and  p[i] + p[j] <= diff:
                return "yes"
    return "no"

t = int(input())
while t:
    n , s = input().split()
    n = int(n)
    s = int(s)
    p = list(map(int,input().split()))
    p_t  = list(map(int,input().split()))
    diff = 100 - s
    print(chef(p,p_t,n,diff))
    t = t - 1
