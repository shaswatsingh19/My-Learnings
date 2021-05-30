// https://leetcode.com/problems/valid-anagram/
class Solution {
    public boolean isAnagram(String s, String t) {
        int [] arr = new int[26];
        for (int i=0;i<s.length();i++){
            char c = s.charAt(i);
            int index = c - 97;
            arr[index] += 1;
        }
        
        System.out.println(Arrays.toString(arr));
        for (int j=0;j<t.length();j++){
            char ch = t.charAt(j);
            int idx = ch - 97;
            arr[idx] -= 1;
        }
        
                System.out.println(Arrays.toString(arr));
        for(int i = 0;i<arr.length;i++){
            if(arr[i]!=0){
                return false;
            }
        }
        return true;
    }
}