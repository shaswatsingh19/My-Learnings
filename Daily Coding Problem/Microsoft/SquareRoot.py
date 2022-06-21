# https://workat.tech/problem-solving/practice/square-root
class Solution:
	def searchRoot(self, n: int) -> int:
		# add your logic here
		
		ans = 0
		s = 0
		e = n
		while(s<=e):
			mid = s + (e-s)//2
			if(mid*mid <= n):
				ans = mid
				
				s = mid + 1
				
			else:
				e = mid-1
			
		return ans