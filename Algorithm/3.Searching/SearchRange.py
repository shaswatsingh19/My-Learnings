# https://workat.tech/problem-solving/practice/search-range
class Solution:
	def searchRange(self, arr: List[int], key: int) -> List[int]:
		# add your logic here
		
		s = 0
		e = len(arr)-1
		i,j = (self.binaryF(arr,s,e,key),self.binaryL(arr,s,e,key,len(arr)))
		return [i,j]
	
	
	def binaryF(self,arr,s,e,key):
		if(s<=e):
			mid = e + (s-e)//2
			if( (mid == 0 or arr[mid-1]<key) and (arr[mid]== key) ):
				return mid
			elif (key > arr[mid]):
				return self.binaryF(arr,mid+1,e,key)
			else:
				return self.binaryF(arr,s,mid-1,key)
		return -1
	
	def binaryL(self,arr,s,e,key,n):
		if(s<=e):
			mid  = e + (s-e)//2
			if( (mid == n-1 or arr[mid+1]>key ) and (arr[mid] == key)):
				return  mid
			elif (arr[mid] > key):
				return self.binaryL(arr,s,mid-1,key,n)
			else:
				return self.binaryL(arr,mid+1,e,key,n)
		return -1
