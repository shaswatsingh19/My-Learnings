# https://www.codechef.com/APRIL20B/problems/COVIDLQ

t = int(input())

for i in range(t):
    li = []
    n = int(input())
    queue  = list(map(int,input().split()))
    for j in range(n):
        if queue[j] == 1:
            li.append(j)
    count = 0
    for k in range(len(li)-1):
        if li[k+1] - li[k] <6:
            count = count + 1
            print("NO")
            break
    if count == 0:
        print("YES")
