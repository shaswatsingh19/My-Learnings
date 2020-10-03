# https://www.codechef.com/QTCC2020/problems/VIEW2004

li = list(map(float,input().split()))
li  = li[1:]
leng = len(li)//2
i = 0
while leng:
    a = li[i:i+2]
    sci = a[0] * (10**(a[1]))
    print("%.2f"%sci)
    print()
    i  = i+2
    
    leng = leng -1
