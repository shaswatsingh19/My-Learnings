# https://workat.tech/problem-solving/practice/sorted-arrays-intersection
class Solution:
	def intersection(self, A: List[int], B: List[int]) -> List[int]:
		# add your logic here
		arr = []
		
		i = 0
		j = 0
		while(i<len(A) and j<len(B)):
			if(A[i] == B[j]):
				arr.append(A[i])
				i+=1
				j+=1
			elif(A[i]<B[j]):
				i+=1
			else:
				j+=1
		return arr//https://workat.tech/problem-solving/practice/largest-contiguous
class Solution {
	int largestContiguousSum(int[] arr){
		int curr = Integer.MIN_VALUE;
		
		int best = 0;
		
		// if every element is negative in array
		for(int i=0;i<arr.length;i++){
			if(arr[i]>curr){
				curr = arr[i];
			}
		}
		if(curr<0)return curr;
		
		// mix of positive and negative
		curr = 0;
		
		for(int i=0;i<arr.length;i++){
			curr+=arr[i];
			if(best<curr){
				best = curr ;
			}
			if(curr<0){
				curr = 0;
			}
		}
		
		return best;
	}
}