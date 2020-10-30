def missing1(nums):
    nums = sorted(nums) + [None]
    for i in range(len(nums)):
        if i != nums[i]:
            return i

# time  = O(nlogn)
# space = O(1)
                
def missing2(nums):
    ans = len(nums)
    for idx,elm in enumerate(nums):
        ans = ans^idx^elm
    
    return ans

# Time:- O(n)
# Space :- O(1)

# another approach is using Gauss'formula which is (n*(n+1))/2
def missing3(nums):
    n = len(nums)
    expected_sum = (n*(n+1))//2
    actual_sum = sum(nums)
    ans = expected_sum-actual_sum
    return ans 


nums= [4,5,0,2,1]
print(missing3(nums))