# https://www.codechef.com/problems/HS08TEST

try:
    t = int(input())
    a = [0]*t
    for i in range(t):
        a[i] = int(input())
    a.sort()
    for i in range(t):
        print(a[i])
except:
    EOFError
