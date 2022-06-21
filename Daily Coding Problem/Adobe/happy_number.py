# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        
        def get_next(num):
            s = 0
            
            while num:
                rem = num%10
                s += rem*rem 
                num = num//10
                
            return s
        
        
        
        slow = n
        fast = get_next(n)
        
        while fast!=1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
            
        return fast == 1
        

#         se = set()
#         while n:
#             if n==1:
#                 return True
#             if n not in se:
#                 se.add(n)
#             else:
#                 return False
            
#             ans = 0
#             while n:
#                 rem = n%10
#                 ans += rem*rem
#                 n = n//10
                
                
#             n = ans
    