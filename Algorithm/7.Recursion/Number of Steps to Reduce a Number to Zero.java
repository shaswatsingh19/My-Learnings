//https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
class Solution {
    public int numberOfSteps(int num) {
        
        int c = 0;
        return ans(num,c);
    }
    
    
    public static int ans(int n , int c){
        if(n == 0) return c;
        
        if(n%2==0) return ans(n/2,c+1);
        return ans(n-1,c+1);
    }
