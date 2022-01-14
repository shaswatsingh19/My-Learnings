// https://workat.tech/problem-solving/practice/positive-cumulative-sum
class Solution {
	List<Integer> getPositiveCumulativeSum (int[] arr) {
		// add your logic here
		List<Integer> l = new ArrayList<>();
		
		if(arr[0]>0){
				l.add(arr[0]);
			}
			
		for(int i=1;i<arr.length;i++){
			arr[i] = arr[i] + arr[i-1];
			if(arr[i]>0){
				l.add(arr[i]);
			}
			
		}
		return l;
	}
}