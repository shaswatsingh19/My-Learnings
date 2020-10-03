# https://www.hackerearth.com/practice/algorithms/string-algorithm/basics-of-string-manipulation/practice-problems/algorithm/monk-teaches-palindrome/

t = int(input())

for i in range(t):
    s = input()
    f = 0
    l  = len(s) - 1
    flag = 0
    while f<l:
        if s[f] == s[l]:
            f = f +1
            l = l -1
            flag = flag + 1
    if flag == len(s)//2 and len(s) % 2 != 0:
        print("YES ODD")
    elif flag == len(s)//2 and len(s) % 2 == 0:
        print("YES EVEN")
    else:
        print("NO")
            
