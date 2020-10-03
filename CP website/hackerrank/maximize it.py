# https://www.hackerrank.com/challenges/maximize-it/problem



k,m = input().split()
k  = int(k)
add  = 0
while k:
    li = list(map(int,input().split()))
    li = li[1:]
    max_li = max(li)
    add = add + pow(max_li,2)
    k = k - 1
print(add%int(m))
