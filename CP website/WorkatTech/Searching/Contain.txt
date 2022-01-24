# https://workat.tech/problem-solving/practice/contains-element/
class Solution:
	def containsElement(self, arr: List[int], key: int) -> bool:
		# add your logic here
		s = 0
		e = len(arr)-1
		while(s<=e):
			mid = e + (s-e)//2
			if(arr[mid]<key):
				s = mid+1
			elif (arr[mid]>key):
				e = mid-1
			else:
				return True
			
		return False
		
		


