num = []    
t =int(input())
for i in range(0,t):
    l = int(input())
    r =int(input())
summ = 0
by =  (r-l) + 1
for i in range(l,r+1):
    summ = summ + l
avgg = summ/by
print(avgg)
num.append(avgg)



    
    
