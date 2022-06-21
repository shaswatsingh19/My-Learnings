// https://leetcode.com/problems/valid-parentheses/
import java.util.*;

class Solution {
    public boolean isValid(String s) {
    
        Stack<Character> stack = new Stack<>();
        
        char first = s.charAt(0);
        if (s.length()<2) return false;
        
        else if ( first == '}' || first == ']' || first == ')') return false;
        
        for(int i=0;i<s.length();i++){
            char ch = s.charAt(i);
            if (ch == '(' || ch=='[' || ch=='{' ){
                stack.push(ch);
            }
            else if ( ch== '}' || ch==']' || ch==')') {
                char peek = '0';
                if (!stack.empty()) peek = stack.peek();
                if (ch== '}' && peek == '{' ){
                    stack.pop();
                }
                else if (ch== ']' && peek == '['){
                    stack.pop();
                }
                else if (ch == ')' && peek== '('){
                    stack.pop();
                }
                else{
                    return false;
                }
                
                
                
            }
        }
        
        
        if (!stack.empty()) return false;
        return true;
    }
}