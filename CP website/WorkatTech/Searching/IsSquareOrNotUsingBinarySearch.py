# https://workat.tech/problem-solving/practice/is-perfect-square/
class Solution:
	def isPerfectSquare(self, n: int) -> bool:
		# add your logic here
		
		s = 0
		e = n 
		while(s<=e):
			mid = s + (e-s)//2
			if(mid*mid == n):
				return True
			elif (mid*mid < n):
				s = mid + 1
			else :
				e = mid - 1
		return False

