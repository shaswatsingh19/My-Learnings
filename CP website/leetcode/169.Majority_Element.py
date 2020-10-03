Problem :	

		Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

		You may assume that the array is non-empty and the majority element always exist in the array.

		Example 1:

		Input: [3,2,3]
		Output: 3
		Example 2:

		Input: [2,2,1,1,1,2,2]
		Output: 2

Solution :
		class Solution:
			def majorityElement(self, nums: List[int]) -> int:
				major = 0
				c = 0
				for i in nums:
					if c == 0:
						major = i
					if major == i:
						c += 1
					else:
						c -= 1
				return major
