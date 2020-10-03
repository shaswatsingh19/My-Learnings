n,m,a = map(int,input().split())

l  = n//a
w = m//a

if n%a != 0:
    l = l+1
if m%a != 0:
    w = w+1
print((l*w))
