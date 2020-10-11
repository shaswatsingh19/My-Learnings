# https://www.codechef.com/COOK117B/problems/LIFTME

def lift_request(q):
    add = 0
    pre_q2 = 0
    while q:
        q1, q2 = input().split()
        q1 = int(q1)
        q2 = int(q2)
        if pre_q2 != q1:
            add = add + abs(q1-q2) + abs(pre_q2-q1)
        else:
            add  = add + abs(q2-q1)    
        pre_q2 = q2
        q = q- 1
    if q2 != 0:
        add = add + q2
        return add
    else:
        return add
    


t = int(input())
while t:
    n,q = input().split()
    n = int(n)
    q = int(q)
    print(lift_request(q))
    t = t -1
