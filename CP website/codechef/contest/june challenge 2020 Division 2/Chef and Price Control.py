t = int(input())
while t:
    n , k = input().split()
    n = int(n)
    k = int(k)
    p = list(map(int,input().split()))
    p.sort()
    no = False
    sum_p = sum(p)
    # p = [1,2,3,4,5,6,7]
    for i in range(len(p)):
        if p[i]> k:
            p_new1 = p[:i]
            p_new2 = [k]*len(p[i:])
            p_new = p_new1 + p_new2
            sum_p_new = sum(p_new)
            print(sum_p - sum_p_new)
            no = True
            break
    if no == False:
        print(0)
        
    t = t - 1
