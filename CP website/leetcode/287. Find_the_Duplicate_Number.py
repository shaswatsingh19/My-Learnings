Problem Link : https://leetcode.com/problems/find-the-duplicate-number/
Problem Description:
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.



SOLUTION :
It is with constant space as i didn't use any other data structures 



class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(size):
            if nums[abs(nums[i])] >=0:
                nums[abs(nums[i])] = -nums[abs(nums[i])]
            else:
                return abs(nums[i])
        
