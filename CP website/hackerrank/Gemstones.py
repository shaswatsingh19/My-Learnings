# https://www.hackerrank.com/challenges/gem-stones/problem

def gemstones(arr):
    gems = set.intersection(*arr)
    return len(gems)


n = int(input())
arr =[]
for  i in range(n):
    arr_item = input()
    arr.append(set(arr_item))
    
result = gemstones(arr)
