//https://workat.tech/problem-solving/practice/even-number-of-digits
class Solution {
	List<Integer> getEvenDigitNumbers (int[] arr) {
		// add your logic here
		ArrayList<Integer> l = new ArrayList<>();
		for(int i=0;i<arr.length;i++){
			if( (arr[i]>9 && arr[i]<100) || (arr[i]>999 && arr[i]<10000) || 
			   (arr[i]>99999 && arr[i]<1000000) ){
				l.add(arr[i]);
			}
		}
		
		return l;
	}
}