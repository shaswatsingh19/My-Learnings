# https://workat.tech/problem-solving/practice/even-number-of-digits
class Solution:
	def getEvenDigitNumbers(self, arr: List[int]) -> Optional[List[int]]:
		# add your logic here
		n  = len(arr)
		even = []
		for i in range(n):
			s  = str(arr[i])
			if(len(s)%2==0):even.append(arr[i])
		return even

