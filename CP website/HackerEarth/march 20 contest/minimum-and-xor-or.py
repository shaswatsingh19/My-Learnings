# https://www.hackerearth.com/challenges/competitive/march-circuits-20/algorithm/minimum-and-xor-or-6a05bbd4/

def minimum(arr):
    arr.sort()
    min_xor = 99999
    val = 0
    for k in range(len(arr)-1):
        r = (arr[k]&arr[k+1])^(arr[k]|arr[k+1])
        min_xor = min(min_xor,r)
    return min_xor

t = int(input())
for i in range(t):
    n = int(input())
    a = []
    a = list(map(int,input().split()))
    print(minimum(a))
