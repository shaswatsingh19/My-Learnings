# https://workat.tech/problem-solving/practice/merge-two-sorted-arrays
class Solution:
	def mergeSortedArrays(self, A: List[int], B: List[int]) -> List[int]:
		# add your logic here
		m = len(A)
		n = len(B)
		C = [0]*(m+n)
		i=0
		j=0
		k=0
		
		while(i<m and j<n):
			if(A[i]<=B[j]):
				C[k] = A[i]
				
				i+=1
			else:
				C[k] = B[j]
				j+=1
			k+=1
		while(i<m):
			C[k] = A[i]
			k+=1
			i+=1
			
		while(j<n):
			C[k] = B[j]
			j+=1
			k+=1
			
			
		return C
