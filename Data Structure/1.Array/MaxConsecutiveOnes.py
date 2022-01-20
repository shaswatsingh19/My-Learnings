# https://workat.tech/problem-solving/practice/max-consecutive-ones
class Solution:
	def getMaxConsecutiveOnes(self, arr: List[int]) -> int:
		# add your logic here
		n = len(arr)
		cnt = 0
		maximum = 0
		for i in range(n):
			if(arr[i]==1):
				cnt+=1
			else:
				maximum = max(cnt,maximum)
				cnt =0
		maximum = max(cnt,maximum)
		return maximum