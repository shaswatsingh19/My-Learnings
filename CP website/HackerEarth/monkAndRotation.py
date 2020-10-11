t = int(input())
while t:
    n,k= map(int,input().split())
    while (k>=n):
        k = k - n
    arr= list(map(int,input().split()))
    for i in range(n-k,n):
        print(arr[i],end=' ')
    for i in range(0,n-k):
        print(arr[i],end=' ')
    print()
 
    t-=1
