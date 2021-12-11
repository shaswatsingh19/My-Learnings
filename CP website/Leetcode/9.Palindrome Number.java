//https://leetcode.com/problems/palindrome-number/solution/
class Solution {
    public boolean isPalindrome(int x) {
        if(x<0) return false;
        int ans=0;
        int temp=x;
        while(temp>0){
            int rem = temp%10;
            ans = ans * 10 + rem;
            temp = temp/10;
            
            
        }
        if(ans==x){
            return true;
        }
        return false;
    }
}