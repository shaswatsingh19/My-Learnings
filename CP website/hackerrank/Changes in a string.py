# https://www.hackerearth.com/challenges/competitive/april-circuits-20/algorithm/ab-string-5f6b213a/

t=int(input())
while t:
    n =int(input())
    s = input()
    s = list(s)
    u =sorted(s)
    c = 0
    i = 0
    b_count = s.count('b')
    while b_count >0 and s!= u:
        if s[i] == 'b':
            s.remove('b')
            s.append('b')
            c = c +1
            b_count = b_count + 1
            i = i -1
        i = i +1
    print(c)
    t = t -1
