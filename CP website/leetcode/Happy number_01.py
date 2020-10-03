# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
'''
def ishappy(n):
    i = 0
    while n!= 1 and i<40:
        q = 0
        while n!= 0:
            q = q+ (n%10)**2
            n  = n//10
            i = i + 1
        n = q
    return n == 1
'''

def ishappy(n):
    dic = dict()
    while n:
        if 1 in dic:
            return True
        elif n in dic:
            return False
        temp = 0
        dic[n] = 0
        while n:
            temp = temp + (n%10)**2
            n = n//10
        n = temp
