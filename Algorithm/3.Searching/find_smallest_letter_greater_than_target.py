# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l= 0
        h = len(letters)-1
        while l<=h:
            mid  = (l+h)//2
            if letters[mid] <= target:
                l = mid+1
                
            else:
                h = mid - 1
                
        if l>=len(letters):
            return letters[0]
        return letters[l]