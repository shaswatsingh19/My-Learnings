//https://workat.tech/problem-solving/practice/largest-contiguous
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