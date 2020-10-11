# https://www.codechef.com/ENCD2020/problems/ECAPR204

t = int(input())
di = {}
while t:
    n = int(input())
    li =  list(map(int,input().split()))
    
    for i in li:
        if i not in di:
            di[i] = 1
        elif i in di:
            di[i] = di[i] + 1
    for k,v in di.items():
        print(str(k)+":"+str(v))
    t = t -1
