# https://workat.tech/problem-solving/practice/cumulative-sum
class Solution:
	def getCumulativeSum(self, arr: List[int]) -> List[int]:
		# add your logic here
		# T = O(n)  S = O(1)
		n = len(arr)
		for i in range(1,n):
			arr[i] = arr[i-1] + arr[i]
		return arr

