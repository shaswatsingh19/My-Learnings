t = int(input())
for i  in range(t):
    n  = list(map(int,input().split()))
    lis = n[1:]
    for i in range(len(lis)-1):
        if lis[i] == -1:
            if (lis[i-1]%2== 0 and lis[i+1] %2==0) or (lis[i-1]%2 !=  0 and lis[i+1]%2 != 0):
                lis[i] = abs(lis[i-1] - lis[i+1])
            else:
                lis[i] = (lis[i-1] + lis[i+1])//2
    for i in range(len(lis) -1):
        if lis[i] != 1:
            lis[i] = lis[i] - 1
    lis = list(map(str,lis))
    lis = ''.join(lis)
    lis = int(lis)
    print(lis)
    
            

