# https://practice.geeksforgeeks.org/problems/reorganize-the-array/0
'''
t = int(input())

while(t):
    n  =  int(input())
    arr = list(map(int,input().split()))
    for i in range(n):
        if (arr[i] != -1 and arr[i] != i):
            x  = arr[i]
            while( arr[x] != -1 and arr[x] != x):
                y = arr[x]
                arr[x] =x
                x =y
            arr[x] =x
            if arr[i] != i:
                arr[i] = -1
    print(arr)
    t= t - 1
    
'''
t = int(input())
while(t):
    s = set()
    n = int(input())
    ar = list(map(int,input().split()))
    for i in range(n):
        s.add(ar[i])
    for i in range(n):
        if i in s:
            ar[i] = i
        else:
            ar[i] = -1
    print(ar)
    
    t =t -1
