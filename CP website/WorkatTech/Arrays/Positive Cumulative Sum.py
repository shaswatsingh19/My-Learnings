# https://workat.tech/problem-solving/practice/positive-cumulative-sum/
class Solution:
	def getPositiveCumulativeSum(self, arr: List[int]) -> List[int]:
		n = len(arr)
		pos = []
		if(arr[0] >0):pos.append(arr[0])
		for i in range(1,n):
			arr[i] = arr[i-1] + arr[i]
			if(arr[i]>0):pos.append(arr[i])
			
		return pos

