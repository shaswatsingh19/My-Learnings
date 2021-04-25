//https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
import java.util.Stack;

class Solution {
    public String removeDuplicates(String S) {
        
        Stack<Character> stk = new Stack<>();
        
        stk.push(S.charAt(0));
        int j=1;
        for(int i =1;i<S.length();i++){
            char c = S.charAt(i);
            if(!stk.isEmpty() && stk.peek() == c){
                stk.pop();
                j-=1;

            }
            else{
                stk.push(c);
                j+=1;
            }
        }
        
     
        StringBuilder ans = new StringBuilder();
        while(!stk.isEmpty()){
            ans.append(stk.pop());
        }
        return ans.reverse().toString();
    }
}