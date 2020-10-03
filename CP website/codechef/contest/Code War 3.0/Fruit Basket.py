# https://www.codechef.com/COW42020/problems/COW3A

t = int(input())
print()
while t:
    a,b,c,d = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    d = int(d)
    apple = d - b
    mango = d -c
    orange = d - a
    print(apple," ",mango," ",orange)
    t = t -1
