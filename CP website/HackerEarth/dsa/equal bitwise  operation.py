# https://www.hackerearth.com/challenges/competitive/data-structures-and-algorithms-coding-contest-april-2020/algorithm/equal-bitwise-operations-33fa5acd/


t = int(input())
n  = list(map(int,input().split()))

for i in range(t-1):
    for  j in range(i+1,t):
        if n[i] & n[j] == n[i]|n[j] and  n[i]|n[j] == n[i]^n[j]:
            print(n[i],n[j])
        
