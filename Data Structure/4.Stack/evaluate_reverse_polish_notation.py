# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        
        stack = []
        i=0
        operator = ("+", "-", "*", "/")
        while i<len(tokens):
            if tokens[i] not in operator:
                stack.append(int(tokens[i]))
                
            else:
                op  = tokens[i]
                first = stack.pop()
                second = stack.pop()
                if op=='+':
                    val = second + first
                elif op == '-':
                    val = second - first
                elif op == '/':
                    val = second / first
                    val = int(val)
                    
                elif op == '*':
                    val = second * first
                stack.append(val)
                    
            i+=1
            
        return stack[-1]
                