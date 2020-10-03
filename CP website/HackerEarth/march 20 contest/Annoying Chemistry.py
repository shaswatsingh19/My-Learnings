def chemical(x,y,p,q):
    # b3 = (b1*x)/p
    # value using x,y,p,q is in
    a = ((y*p)/(x*q))
    b1 = [1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0]
    for i in range(1,11):
        b2 = i
        val = b2 * a
        if val in b1:
            b3 = (val*x)/p
            b4 = (b2*y)/q
            if b3 == b4:
                print(int(val),int(b2),int(b3))
                return
                      


x,y,p,q = map(int,input().split())
chemical(x,y,p,q)
