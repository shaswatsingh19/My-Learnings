# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/micro-and-array-update/
t = int(input())
while t:
    n,k = map(int,input().split())
    a = min(list(map(int,input().split())))
    if a>=k:
        print(0)
    else:
        print(k-a)
    t = t -1
