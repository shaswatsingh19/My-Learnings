# https://workat.tech/problem-solving/practice/remove-occurences/
class Solution:
	def removeOccurences(self, arr: List[int], k: int) -> int:
		# add your logic here
		
		n = len(arr)
		
		i = n-1
		j = n-1
		while(j>-1):
			if(arr[j] == k  ):
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp
				i-=1
				j-=1
			elif(arr[j] != k ):
				j-=1;
		return i+1
	
# 		count_k = 0
# 		n = len(A)
# 		for i in range(n):
# 			if(A[i] == k):
# 				count_k += 1
# 		return n-count_k