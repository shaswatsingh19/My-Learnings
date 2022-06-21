//https://workat.tech/problem-solving/practice/arithmetic-sequence
class Solution {
	boolean isArithmeticSequence (int[] arr) {
		// add your logic here
		Arrays.sort(arr);
		int d=0;
		if(arr.length>1){
		
			d=arr[1]-arr[0];	
		}else{return true;}
		for(int i=1;i<arr.length-1;i++){
			if(arr[i+1]-arr[i] != d){
				return false;
			}
			
		}
		
		return true;
	}
}