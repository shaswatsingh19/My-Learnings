// https://leetcode.com/problems/shuffle-string/
class Solution {
    public String restoreString(String s, int[] indices) {
        int l = indices.length;
        // char [] arr = new char[l];
        // for(int i=0;i<l;i++){
        //     arr[indices[i]] = s.charAt(i);
        // }
        // return new String(arr);
        
        
        StringBuilder sb = new StringBuilder(s);
        for(int i=0;i<l;i++){
            sb.setCharAt(indices[i],s.charAt(i));
        }
        
        return new String(sb);
    }
}