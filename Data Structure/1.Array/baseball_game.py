# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for i in ops:
            if i=='C':
                stack.pop()
            elif i=='D':
                el = stack[-1]
                stack.append(el*2)
            elif i=='+':
                last = stack[-1]
                secLast = stack[-2]
                stack.append(last+secLast)
                
            else:
                stack.append(int(i))
                
        return sum(stack)
        