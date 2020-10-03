t = int(input())
a =[0]*t
for  i in range(t):
    a[i] = int(input())
a.sort()
maxi = 0
for j in range(t):
    s = a[j]*(t-j)
    if s>maxi:
        maxi = s
print(maxi)

