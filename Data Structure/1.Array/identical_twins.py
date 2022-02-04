class Solution:
	def getIdenticalTwinsCount(self, arr: List[int]) -> int:
		# add your logic here
		# O(N*N) O(1)
		# n = len(arr)
		# cnt = 0
		# for  i in range(n):
		# 	for j in range(i+1,n,1):
		# 		if(arr[i] == arr[j]):
		# 			cnt+=1
		# return cnt
		cnt=0
		n = len(arr)
		di = {}
		for i in range(n):
			if(arr[i] not in di):
				di[arr[i]] = 1
			else:
				di[arr[i]] += 1
		# print(di)
		for k,v in di.items():
			if(v>1):
				# here we are finding Nc2 = fact(N)/ fact(2)*fact(N-2)
				cnt += (v*(v-1))//2
		return cnt
		
		
		



