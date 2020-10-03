# https://www.codechef.com/JUNE20B/problems/EOEO

t = int(input())
while t:
    ts = int(input())
    if ts % 2 == 0:
        i = 4
        c = 0
        k = 2
        while i <= ts:
            c = c + 1
            i = i + pow(2,k)
            k = k + 1
        print(c)
            
    elif ts % 2 != 0:
        print(ts//2)
     t = t -1
