# https://workat.tech/problem-solving/practice/non-repeating-element
class Solution:
	def findNonRepeatingElement(self, arr: List[int]) -> int:
		# add your logic here
		
		ans = 0
		for i in arr:
			ans = ans^i
			
		return ans

