//https://workat.tech/problem-solving/practice/merge-two-sorted-arrays/
class Solution {
	int[] mergeSortedArrays(int[] A, int[] B) {
	    // add your logic here
		int [] C = new int [A.length+B.length];
		int a=0;
		int b=0;
		int c=0;
		
		while(a<A.length && b<B.length){
			if(A[a] <= B[b]){
				C[c] = A[a];
				c++;
				a++;
			}else{
				C[c] = B[b];
				c++;
				b++;
			}
		}
		while(a<A.length){
			C[c] = A[a];
			a++;
			c++;
		}
		
		while(b<B.length){
			C[c] = B[b];
			b++;
			c++;
		}
		
		return C;
	}
}