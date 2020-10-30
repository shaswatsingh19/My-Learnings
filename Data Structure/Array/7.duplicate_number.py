'''
How do you find the duplicate number on a given integer array
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one duplicate number in nums, return this duplicate number.
'''
def duplicate1(lst):
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            return lst[i]

# time :- O(nlogn)
# space :- O(1)

def duplicate2(lst):
    di = {}
    for i in lst:
        if i not in di:
            di[i] = 1
        else:
            di[i] += 1

    for k,v in di.items():
        if v>1:
            return k

# time :- O(n)
# space :- O(n)


def duplicate3(lst):
    n = len(lst)
    excepted_sum = (n*(n+1))//2
    actual_sum = sum(lst)
    ans  = n - (excepted_sum-actual_sum)
    return ans

# time :- O(n)
# space :- O(1)



arr = [1,2,3,3]
print(duplicate1(arr))