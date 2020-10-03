# https://www.hackerrank.com/challenges/python-lists/problem

c = int(input())
l = []
while c:
    q = input().split()
    if q[0] == 'insert':
        i = int(q[1])
        e = int(q[2])
        l.insert(i,e)
    elif q[0] == 'print':
        print(l)
    elif q[0] == 'remove':
        e = int(q[1])
        l.remove(e)
    elif q[0] == 'append':
        e = int(q[1])
        l.append(e)
    elif q[0] == 'sort':
        l.sort()
    elif q[0] == 'pop':
        l.pop()
    elif q[0] == 'reverse':
        l.sort(reverse= True)
    c = c -1
