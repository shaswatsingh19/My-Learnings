# https://www.hackerrank.com/challenges/find-digits/problem

t = int(input())
while t:
    n = int(input())
    cnt = 0
    temp = n
    while n:
        digit = n%10
        if digit == 0:
            pass
        
        elif temp % digit  == 0:
            cnt = cnt + 1
        n = n //10
    print(cnt)
        
    t = t -1
