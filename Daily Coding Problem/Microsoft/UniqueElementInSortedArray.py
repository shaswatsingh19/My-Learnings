# https://workat.tech/problem-solving/practice/unique-elements-sorted-array
class Solution:
	def removeDuplicates(self, A: List[int]) -> int:
		# add your logic here
		# O(N) time and SPace
# 		di = {}
# 		for i in range(len(A)):
# 			if A[i] not in di:
# 				di[A[i]] = 1
				
# 		return len(di)
		
	
		# O(N) time and O(1)
		i = 0
		j = len(A)-1
		cu = len(A)
		while(i<j):
			while(i!=j and A[i] == A[i+1]):
				i+=1
				cu-=1
			while(i!=j and A[j] == A[j-1]):
				j-=1
				cu-=1
			i+=1
			
		return cu