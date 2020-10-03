# https://www.hackerrank.com/challenges/collections-counter/problem
from collections import Counter
x = int(input())
size = list(map(int,input().split()))
size  = Counter(size)
c  = int(input())
income = 0
while c:
    s,p = input().split()
    s = int(s)
    p = int(p)
    if size[s] > 0:
        size[s] = size[s] - 1
        income  =income + p
    c = c -1
