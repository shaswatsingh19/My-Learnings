# https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen

n = int(input())
a = set(map(int,input().split()))
m  = int(input())
for i in range(m):
    query  = input().split()
    query = list(query)
    other  = set(map(int,input().split()))
    if query[0] == 'intersection_update':
        query[1] = int(query[1])
        a.intersection_update(other)
    elif query[0] == 'update':
        query[1] = int(query[1])
        a.update(other)
    elif query[0] == 'symmetric_difference_update':
        a.symmetric_difference_update(other)
    elif query[0] == 'difference_update':
        a.difference_update(other)
a = list(a)
print(sum(a))
    
