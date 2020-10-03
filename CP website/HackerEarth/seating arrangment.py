times = int(input())
sin= []
sout = []
for i in range(times):
    seat = int(input())
    sin.append(seat)
    x = sin[i]%12
    
    if(x ==0 or x== 1 or x == 2  or x==3 or  x==4 or x ==5  or x ==6 or x== 7 or x ==8 or x==9 or x==10 or x==11):
        if(x==0):
            seat =seat - 11
        elif(x==1):
            seat =seat + 11
        elif(x==  2):
            seat = seat + 9
        elif(x==3):
            seat =seat + 7
        elif(x==4):
            seat =seat + 5
        elif( x == 5):
            seat = seat + 3
        elif(x==6):
            seat = seat + 1
        elif(x == 7):
            seat = seat -  1
        elif(x==8):
            seat =seat - 3
        elif(x ==9):
            seat = seat -5
        elif(x==10):
            seat = seat -7
        else:
            seat = seat - 9
            
        sout.append(seat)
        
for i  in sout:
    y = i%12
    if(y== 0 or y==1 or y==6 or y==7):
        print(i, end= " ")
        print("WS")
    elif(y==2 or y==5 or y ==8or y ==11):
        print(i, end = " ")
        print("MS")
    else:
        print(i, end = " ")
        print("AS")
    
            
        
        
    
        
    
