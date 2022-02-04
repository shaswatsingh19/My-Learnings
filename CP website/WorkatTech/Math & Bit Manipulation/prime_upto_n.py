# https://workat.tech/problem-solving/practice/primes-upto-n/editorial
class Solution:
	def primesUptoN(self, n: int) -> List[int]:
		# add your logic here
		
		prime = []
		for i in range(2,n+1):
			check = True
			j = 2
			while(j*j<=i):
				if(i%j==0):
					check = False
					break
				j+=1
					
			if(check):
				prime.append(i)
		
		return prime
			