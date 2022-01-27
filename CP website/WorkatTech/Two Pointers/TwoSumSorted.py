# https://workat.tech/problem-solving/practice/two-sum-sorted
class Solution:
	def hasTwoSumZero(self, arr: List[int]) -> bool:
		i = 0
		j = len(arr)-1
		while(i<j):
			if(arr[i]+arr[j]==0):
				return True
			elif(arr[i]+arr[j]>0):
				j-=1
			else:
				i+=1
		return False
		


