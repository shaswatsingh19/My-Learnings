# https://www.codechef.com/JUNE20B/problems/XYSTR

t = int(input())
while t:
    s = input()
    c = 0
    i = 0
    while i < (len(s) - 1):
        if s[i] != s[i+1]:
            c += 1
            i += 2
        elif s[i] == s[i+1]:
            i = i + 1
    print(c)
        
    t = t -1
