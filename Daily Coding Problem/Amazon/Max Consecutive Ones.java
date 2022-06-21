//https://workat.tech/problem-solving/practice/max-consecutive-ones/editorial
class Solution {
	int getMaxConsecutiveOnes(int[] A) {
	    // add your logic here
		int max = 0;
		int cnt = 0;
		for(int i=0;i<A.length;i++){
			if(A[i] == 1){
				cnt++;
			}
			else if(max<cnt && A[i] != 1){
				max = cnt;
				cnt=0;
			}else{cnt=0;}
		}
		if(max<cnt){
			max=cnt;
		}
		return max;
	}
}