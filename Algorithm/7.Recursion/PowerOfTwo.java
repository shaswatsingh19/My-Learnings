//https://leetcode.com/problems/power-of-two/submissions/
class Solution {
    public boolean isPowerOfTwo(int n) {
        
        if(n<1) return false;
        return result(n,0);
    }
    
    public boolean result(int n,int i){
        if((i==0 && n==1) || (i!=0 && n==2)){
            return true;
        }
        
        int rem = n%2;
        if(rem == 0){
            n = n / 2;
            return result(n,i++);
        }
        return false;
    }
    
    
    
}