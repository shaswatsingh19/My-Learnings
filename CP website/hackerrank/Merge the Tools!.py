# https://www.hackerrank.com/challenges/merge-the-tools/problem

n = input()
k = int(input())
split = len(n)//k
c = k
i = 0
while k <= len(n):
    t   = n[i:k]
    i = k
    k = k +c
    num =""
    for j in range(len(t)):
        if t[j] not in num:
            num = num + t[j]
    print(num)
    
