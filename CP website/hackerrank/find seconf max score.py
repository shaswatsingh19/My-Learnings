n = int(input())
a = [int(x) for x  in input().split() ]

m = max(a)
i = 0
length = len(a)
while i < length:
    if ( a[i] == m):
        a.remove(m)
        length = length - 1
        continue
    i = i+1
    
print(max(a))
