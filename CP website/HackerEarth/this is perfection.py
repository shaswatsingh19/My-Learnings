n = int(input())
val = []
for  i in range(n):
    m = int(input())
    val.append(m)


for i in range(n):
    temp = val[i]
    summ = 0
    for j in range(1,temp+1):
        if(temp%j == 0):
            summ = summ + j
        if(temp == summ):
            print("YES")
            break
        if(summ  >  temp):
            print("NO")
            break
        
