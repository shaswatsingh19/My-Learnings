n = int(input())
s = set(map(int, input().split()))
m = int(input())
for i in range(m):
    q = input().split()
    q = list(q)
    if q[0] == 'pop':
        s.pop()
    elif q[0] == 'remove':
        e = int(q[1])
        s.remove(e)
    elif q[0] == 'discard':
        e = int(q[1])
        s.discard(e)
    print(s)
s = list(s)
print(sum(s))
