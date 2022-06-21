# https://workat.tech/problem-solving/practice/next-greater-element-in-sorted-array
class Solution:
	def getNextGreaterElement(self, arr: List[int], key: int) -> int:
		# add your logic here
		n = len(arr)
		if(key>=arr[-1]):
			return key
		elif(key<arr[0]):
			return arr[0]
		ans = -1
		return self.binary(arr,0,n-1,key,ans)
		
	def binary(self,arr,s,e,key,ans):
		if(s<=e):
			mid = s + (e-s)//2
			
			if(arr[mid]<=key):
				return self.binary(arr,mid+1,e,key,ans)
			else:
				return self.binary(arr,s,mid-1,key,arr[mid])
				
		return ans
