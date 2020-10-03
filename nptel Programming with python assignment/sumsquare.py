def sumsquare(l):
    l2 = []
    odd= 0
    even = 0
    for  i in l:
        if( i%2 != 0):
            odd = odd + i*i
        elif(i%2 == 0):
            even = even + i*i
    l2.append(odd)
    l2.append(even)
    print(l2)
        
