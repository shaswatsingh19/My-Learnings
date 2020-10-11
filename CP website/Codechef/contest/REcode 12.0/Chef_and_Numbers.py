# https://www.codechef.com/RC122020/problems/RECNDNOS

t = int(input())
while t:
    di = {}
    n = int(input())
    arr = list(map(int,input().split()))
    for i in range(len(arr)):
            di[i] = arr[i]
    
    t = t -1
