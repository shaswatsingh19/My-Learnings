# https://workat.tech/problem-solving/practice/two-sum/
class Solution:
	def twoSum(self, A: List[int], target: int) -> List[int]:
		# add your logic here
		di = {}
		a = [0,0]
		n = len(A)
		for i in range(n):
			val = target - A[i] # target - A[i] 5 - 1 = 4
			if val not in di:
				di[A[i]] = i
			else:
				a[0] = di[val]
				a[1] = i
				break
			
		return a
			
			


