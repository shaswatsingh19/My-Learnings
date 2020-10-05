# https://www.codechef.com/problems/FLOW016
# a*b = LCM(a,b) * GCD(a,b)
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
t = int(input())
while t:
    a,b = map(int,input().split())
    g = gcd(a,b)
    prod = a*b
    lcm = prod// g
    print(g,lcm)
    t -= 1