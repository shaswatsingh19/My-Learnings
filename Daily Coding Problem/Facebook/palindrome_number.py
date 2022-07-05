# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x<0:
            return False
        elif x>-1 and x<10:
            return True
        
        newNum = 0
        temp = x
        while temp:
            rem = temp%10
            newNum = newNum*10 + rem
            temp//= 10
            
        
        return newNum == x