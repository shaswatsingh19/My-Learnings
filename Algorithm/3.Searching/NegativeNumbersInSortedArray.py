# https://workat.tech/problem-solving/practice/negative-numbers-in-sorted-array/
class Solution:
	def getNegativeNumbersCount(self, arr: List[int]) -> int:
		# add your logic here
		n = len(arr)
		i  = 0
		j = 0
		if(arr[0]<0):
			i = 0
		else:
			return 0
		
		j  = self.binary(arr,0,n-1,n)
		return (j-i+1)

	def binary(self,arr,s,e,n):
		if(s<=e):
			mid  = e + (s-e)//2
			if((mid == 0 or mid == n-1 or arr[mid+1]>= 0 ) and (arr[mid]<0)):
				return mid
			elif(arr[mid]>=0):
				return self.binary(arr,s,mid-1,n)
			else:
				return self.binary(arr,mid+1,e,n)
		return -1
		


