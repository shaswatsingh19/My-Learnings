# https://www.codechef.com/RC122020/problems/RECNDSTR

def left(s):
    s = list(s)
    temp = s[0]
    new = ""
    for i in range(len(s)-1,0,-1):
        new = new + s[i] 
    new = new + temp
    return new
def right(s):
    s = list(s)
    temp = s[len(s)-1]
    new = ""
    new = new + temp
    for i in range(0,len(s)-1):
        new = new + s[i]
    return new
    
t  =int(input())
while t:
    s  = input()
    l = left(s)
    r = right(s)
    if l == r:
        print("YES")
    else:
        print("NO")
    t = t -1
