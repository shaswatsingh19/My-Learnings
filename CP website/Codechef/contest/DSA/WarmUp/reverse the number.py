# https://www.codechef.com/LRNDSA01/problems/FLOW007

def reverse(num):
    s = ""
    while num > 0:
            rem = num %10
            s= s+str(rem)
            num  = int(num /10)
    return int(s)

try:
    t = int(input())
    for  i in range(t):
        num = int(input())
        print(reverse(num))
    
except:
    EOFError
