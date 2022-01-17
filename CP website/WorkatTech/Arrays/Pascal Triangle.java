//https://workat.tech/problem-solving/practice/pascals-triangle/
class Solution {
	int[] pascalTriangleRow(int rowNo) {
		int [] arr = new int[rowNo];
		
		// for(int colNo=1;colNo<=rowNo;colNo++){
		// 	int val = fact(rowNo-1,colNo-1);
		// 	arr[colNo-1] = (val);
		// }
		// return arr;
		
		arr[0] =1;
		rowNo--;
		for(int i=1;i<=rowNo;i++){
			arr[i] = arr[i-1]*(rowNo - i + 1)/i;
		}
		return arr;
	}
	
// 	public static int fact(int n,int c){
		
// 		if(c<=0 || c>=n) return 1;
// 		int ans = 1;
		
// 		c = Math.min(c,n-c);// to reduce only half the results 
		
// 		for(int i=1;i<=c;i++){
// 			ans = (ans*n)/i;
// 			n-=1;
// 		}
		
		
// 		return ans;
// 	}
}