// https://leetcode.com/problems/valid-palindrome/
class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        String s1 = s.replaceAll("[^a-zA-Z0-9]","");
        System.out.println(s1);
        char last = ' ';
        char first = ' ';
        int i = 0;
        int j  = s1.length()-1;
        while(i<j){
            first =s1.charAt(i);
            last = s1.charAt(j);
            if(first == last){
                i++;
                j--;
            }
            else{
                return false;
            }
        }
        return true;
    }
}