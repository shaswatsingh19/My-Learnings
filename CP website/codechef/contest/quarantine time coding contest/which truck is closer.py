# https://www.codechef.com/QTCC2020/problems/VIEW2002

t = int(input())
while t:
    x1,y1,x2,y2 = map(int,input().split())
    a = x1**2 + y1**2
    b = x2 **2 + y2**2
    if a > b:
        print("B IS CLOSER")
    else:
        print("A IS CLOSER")
    t = t- 1
    
