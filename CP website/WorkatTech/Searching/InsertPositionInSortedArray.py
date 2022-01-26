# https://workat.tech/problem-solving/practice/insert-position-in-sorted-array
class Solution:
	def getInsertPosition(self, arr: List[int], key: int) -> int:
		# add your logic here
		n = len(arr)
		s = 0
		e = n-1
		if(key<=arr[0]):
			return 0
		if(key>=arr[n-1]):
			return n
		
		while(s<=e):
			mid = s + (e-s)//2
			if(arr[mid]<key and arr[mid+1]>=key):
				return mid+1
			elif(arr[mid]>=key):
				e = mid-1
			else:
				s = mid +1
		


