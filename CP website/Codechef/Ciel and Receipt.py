# https://www.codechef.com/problems/CIELRCPT
import math

t = int(input())
for  i in range(t):
    a = int(input())
    b = 0
    while (a!=0):
        power  = math.floor(math.log(a,2))
        if power >11:
            power = 11
        a = a -pow(2,power)
        b = b + 1
    print(b)
        
