// https://leetcode.com/problems/check-if-word-equals-summation-of-two-words/
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a1=""
        a2=""
        for i in firstWord:
            a1 += str(ord(i)-97)
        
        a1 = int(a1)
        for i in secondWord:
            a2 += str(ord(i)-97)
        a2 = int(a2)
        
        a3 = ""
        for i in targetWord:
            a3 += str(ord(i)-97)
        a3 = int(a3)
        if(a1+a2 == a3):
            return True
        return False