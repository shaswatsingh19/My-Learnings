# https://leetcode.com/explore/featured/card/30-day-leetcoding-challenge/528/week-1/3285/

'''
li = [-2,1,-3,4,-1,2,1,-5,4]

i = 0
l = len(li)
maxi = -99999'''
# brute force
def max_sub_array(li,n):
    ans = -9999999
    for sub_array_size in range(1,n+1):
        for start_index in range(0,n):
            if sub_array_size + start_index > n:
                break
            add = 0
            for k in range(start_index,start_index + sub_array_size):
                add = add + li[k]
            ans = max(ans,add)
    return ans




li = [1,2,-1,2,-3,4,-5]
n =len(li)
print(max_sub_array(li,n))
