t = int(input())
for i in range(t):
    a,b = map(int,input().split())
    rem = a%b
    if rem == 0:
        print(rem)
    else:
        change = b -rem
        print(change)
    
