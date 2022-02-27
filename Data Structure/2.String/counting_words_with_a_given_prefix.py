# https://leetcode.com/problems/counting-words-with-a-given-prefix/
class Solution:
    def prefixCount(self, w: List[str], p: str) -> int:
        cnt=0
        for i in w:
            print(i[:len(p)])
            if p == i[:len(p)]:
                cnt+=1
                
        return cnt