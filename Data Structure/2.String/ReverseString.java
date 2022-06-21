// https://leetcode.com/problems/reverse-string/
class Solution {
    
    public static void swap(int i,int n,char [] s){
        char t = s[i];
        s[i] = s[n];
        s[n] = t;
    }
    
    public void reverseString(char[] s) {
        
        int n  =  s.length;
        for(int i=0;i<n/2;i++){
            swap(i,n-i-1,s);
            
        }
        
    }
}