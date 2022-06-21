# https://workat.tech/problem-solving/practice/k-subarray-sum/
class Solution:
	def kSubarraySum(self, a: List[int], k: int) -> List[int]:
		
		n = len(a)
		s = 0
		arr = [0] * (n-k+1)
		for i in range(k):
			s += a[i]
		arr[0] = s
		x = 1
		i = 1
		j = k
		while(j<n):
			arr[x] = arr[x-1] - a[i-1] + a[j]
			x+=1
			i+=1
			j+=1
			
		return arr
