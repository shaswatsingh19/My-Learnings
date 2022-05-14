# https://leetcode.com/problems/daily-temperatures/
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        
        
        stack = []
        ans = [0]*len(temp)
        stack.append(len(temp)-1)
        i = len(temp)-2
        while i>-1:
            if not stack:
                stack.append(i)
                i-=1

            elif temp[i] >= temp[stack[-1]]:
                stack.pop()

            else:
                val = stack[-1] # 76
                stack.append(i) # 
                ans[i]  = val - i #4
                i-=1
                
        return ans
                