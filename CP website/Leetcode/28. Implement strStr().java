// https://leetcode.com/problems/implement-strstr/
class Solution {
    public int strStr(String haystack, String needle) {
        int i = 0;
        int j  =0;
        int n  = needle.length();
        int m = haystack.length();
        if(n==0){
            return 0;
        }
        while(j<=m-n){
            String sub = haystack.substring(i,j+n);
            if (sub.equals(needle)){
                return i;
            }
            i++;j++;
        }
        return -1;
        
    }
}