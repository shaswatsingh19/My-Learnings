# https://workat.tech/problem-solving/practice/maximum-k-subarray-sum
class Solution:
	def maxKSubarraySum(self, a: List[int], k: int) -> int:
		n = len(a)
		s = 0
		arr = [0] * (n-k+1)
		for i in range(k):
			s += a[i]
		arr[0] = s
		x = 1
		i = 1
		j = k
		maximum = arr[0]
		while(j<n):
			arr[x] = arr[x-1] - a[i-1] + a[j]
			maximum = max(maximum,arr[x])
			x+=1
			i+=1
			j+=1
			
		return maximum
