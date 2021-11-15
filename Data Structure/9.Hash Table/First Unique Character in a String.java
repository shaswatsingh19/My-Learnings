// https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution {
    public int firstUniqChar(String s) {
        
        int [] arr = new int[26];
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            int index = c - 97;
            arr[index]+=1;
        }
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            
            int index = c - 97;
            if(arr[index]==1){
                return i;
            }
           
        }
        
        
        return -1;
    }
}