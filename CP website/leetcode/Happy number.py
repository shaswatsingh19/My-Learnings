# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3284/
def happy(n,add):
    while n >0:
        rem= n%10
        add = add + rem**2
        n = n //10
    if n == 0 and add != 1:
        flag = False
        return happy(add,0)
    elif add == 1:
        flag = True
        return flag
    

    


n = int(input())
add = 0
print(happy(n,add))
