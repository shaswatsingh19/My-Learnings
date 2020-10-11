# https://www.codechef.com/JUNE20B/problems/CHFICRM
'''
def ice(n,p):
    # p = [5,10,5,5,5,5,15]
    change = 0
    price = 5
    di = {0:0 , 5:0,10:0 ,15:0}
    if p[0] != 5:
        return "NO"
    else:
        for i in range(n):
            if p[i] == price:
                di[price] = di[price] + 1
            else:
                change = p[i] - price
                if di[change] > 0 :
                    di[change] = di[change] - 1
                elif di[price]*price >= change:
                    di[price] = di[price] - 2
                else:
                    return "NO"
    return "YES" 
                
'''
'''
def ice(n,p):
    di = {5:0}
    price = 5
    change = 0
    if p[0] != 5 :
        return "NO"
    else:
        for i in range(n):
            if p[i] == 5:
                di[p[i]] = di[p[i]] + 1
            else:
                change = p[i] - price
                if change <= di[price]*price:
                    di[price] = di[price] - change//5 
                else:
                    return "NO"
    return "YES"
'''
'''
def ice(n,p):
    di = {5:0}
    price = 5
    change = 0
    5,10,5,15
    if p[0] != 5:
        return "NO"
    else:
        for i in range(n):
            if p[i] == 5:
                d[p[i]] = d[p[i]] + 1
            elif p[i] == 10 and d[5]>= 1:
                di[5] = di[5] - 1
            elif p[i] == 15 and d[5] >= 2:
                d[5] = d[5] - 2
            else:
                return "NO"
    return "YES"
            
            
        

t = int(input())

while t:
    n = int(input())
    p = list(map(int,input().split()))
    print(ice(n,p))
    t = t - 1
'''
def ice(n,p):
    di = {5:0,10:0,15:0}
    if p[0] != 5:
        return "NO"
    else:
        for i in range(n):
            if p[i] == 5:
                di[p[i]] = di[p[i]] + 1
            elif p[i] == 10 and di[5]>= 1:
                di[5] = di[5] - 1
                di[10] = di[10] + 1
            elif p[i] == 15 and di[5] >= 2:
                di[5] = di[5] - 2
                di[15] =di[15] + 1
            elif p[i] == 15 and di[10] >= 1:
                di[10] = di[10] - 1
                di[15] = di[15] + 1
            else:
                return "NO"
    return "YES"
    
t = int(input())

while t:
    n = int(input())
    p = list(map(int,input().split()))
    print(ice(n,p))
    t = t - 1
