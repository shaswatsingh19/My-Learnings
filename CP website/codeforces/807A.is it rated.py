# https://codeforces.com/contest/807/problem/A
def rated(t):
    f = []
    s =[]
    for i in range(t):
        a,b = map(int,input().split())
        f.append(a)
        s.append(b)

        if (f[i] != s[i]):
            print("rated")
            return
    for i in range(1,t):
        if f[i] > f[i-1]:
            print("unrated")
            return
    print("maybe")

            

t = int(input())
rated(t)
