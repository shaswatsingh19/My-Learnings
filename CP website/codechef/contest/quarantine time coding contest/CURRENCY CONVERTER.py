
t  = int(input())

while t:
    n = input().split()
    val = int(n[0])
    if n[1] == 'POUNDS':
        ans = val*.84
        print("$"+str(val)+" CONVERTS TO "+str(ans)+" POUNDS")
        

    elif n[1] ==  'LIRA':
        ans = val*2040
        print("$"+str(val)+" CONVERTS TO "+str(ans)+" LIRA")

    elif n[1] == 'FRANCS':
        ans = val*9.85
        print("$"+str(val)+" CONVERTS TO "+str(ans)+" FRANCS")

    elif n[1] == 'MARKS':
        ans = val*3.23
        print("$"+str(val)+" CONVERTS TO "+str(ans)+" MARKS")

    elif n[1] ==  'YEN':
        ans = val*260      
        print("$"+str(val)+" CONVERTS TO "+str(ans)+" YEN")
    t = t -1
