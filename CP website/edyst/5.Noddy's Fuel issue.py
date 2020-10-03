t = int(input())
for i in range(t):
    n = list(map(int,input().split()))
    n = n[1:]
    f = int(input())
    k = int(input())
    sum =  0
    n.sort()
    for  j in range(len(n)):
        sum = sum + n[j]
        k = k -1
        if sum >= f and k != 0:
            print("Yes")
            break
        elif k == 0 :
            print("No")
            break
            
        
