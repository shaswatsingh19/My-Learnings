# https://workat.tech/problem-solving/practice/merge-sorted-subarrays/
class Solution:
	def merge(self, arr: List[int], endIndex: int) -> List[int]:
		# add your logic here
		n = len(arr)
		s = [0]*n
		i = 0
		j = endIndex+1
		k = 0
		while(i<=endIndex and j<n):
			if(arr[i]<=arr[j]):
				s[k] = arr[i]
				i+=1
			else:
				s[k] = arr[j]
				j+=1
			k+=1
		while(i<=endIndex):
			s[k]=arr[i]
			i+=1
			k+=1
		while(j<n):
			s[k]=arr[j]
			j+=1
			k+=1
		return s

