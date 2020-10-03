# https://practice.geeksforgeeks.org/problems/reverse-the-string/0
'''
t = int(input())
while t:
    s = input()
    a =list(s)
    a.reverse()
    print("".join(a))
    
    t = t -1
'''

t = int(input())
while(t):
    s = input()
    f = 0
    l = len(s) - 1
    s = list(s)
    while f<l:
        s[f],s[l] = s[l] ,s[f]
        f = f+ 1
        l = l -1
    print("".join(s))
        
        
    t = t - 1
