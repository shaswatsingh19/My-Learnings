# https://practice.geeksforgeeks.org/contest-problem/satisfy-the-condition/0/
#n*an ≡ b (mod p)
# it means that (mod p) is used in both equations
t= int(input())
for i in range(t):
    a,b,p,x = map(int,input().split())
    n = 1
    count = 0
    while n <= x:
        if (n*(a**n))%p == b%(p):
            count = count  +1
        n = n + 1
    print(count)
