# https://www.hackerrank.com/challenges/alternating-characters/problem?h_l=interview&playlist_slugs%5B%5D=virtusa

t = int(input())
for i in range(t):
    count  = 0
    s = input()
    a = list(s)
    for j in range(len(s)-1):
        f = s[j]
        se = s[j+1]
        if f == se:
            a.remove(f)
            count = count + 1
    print(count)
        
