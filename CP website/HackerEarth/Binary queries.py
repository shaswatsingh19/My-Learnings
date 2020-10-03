# https://www.hackerearth.com/practice/data-structures/arrays/1-d/practice-problems/algorithm/range-query-2a,b =map(int,input().split())
n,q = map(int,input().split())
l = input().split()
for _ in range(q):
    x = list(map(int,input().split()))
    if x[0] == 1 :
        if l[x[1] - 1] =='1':
            l[x[1] - 1 ]='0'
        else:
            l[x[1]-1 ]= '0'
    else:
        num = l[x[2]-1 ]
        if num == '0':
            print("EVEN")
        else:
            print("ODD")
