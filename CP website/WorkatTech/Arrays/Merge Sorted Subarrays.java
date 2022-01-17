//https://workat.tech/problem-solving/practice/merge-sorted-subarrays
class Solution {
	void merge (int[] arr, int endIndex) {
		// add your logic here
		int i=0;
		int j=endIndex+1;
		int [] c = new int[arr.length];
		int k=0;
		
		while(i<=endIndex && j<arr.length){
			if(arr[i]<=arr[j]){
				c[k] = arr[i];
				i++;
			}
			else{
				c[k] = arr[j];
				j++;
			}
			k++;
		}
		
		while(i<=endIndex){
			c[k]=arr[i];
			i++;k++;
		}
		while(j<arr.length){
			c[k]=arr[j];
			k++;j++;
		}
		
		for(i=0;i<arr.length;i++){
			arr[i] = c[i];
		}
		
	}
}