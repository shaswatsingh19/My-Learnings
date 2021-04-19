import java.util.Stack;

public class BalancedParenthesis {
    public static void main(String[] args) {
        Stack <Character> stack = new Stack<>();

        String str  = "{>";
        char peek = '1';
        
        
        for (int i = 0; i < str.length(); i++) {
            char ch = str.charAt(i);
           
            if(ch == '(' || ch=='{' || ch=='[' || ch == '<'){
                stack.push(ch);
                peek = stack.peek();
            }
            else if (ch == ')' &&  peek== '('){
                    stack.pop();
                
            }
            else if (ch == '}' &&  peek== '{'){
                stack.pop();
            
            }
            else if (ch == ']' &&  peek== '['){
                stack.pop();
            
            }
            else if (ch == '>' &&  peek== '<'){
                stack.pop();
            
            }
            else{
                break;
            }

        }
        if(stack.empty()){
            System.out.println("BALANCED PARENTHESIS");
        }
        else{
            System.out.println("INVALID PARENTHESIS");
        }
        
        
    }
}
