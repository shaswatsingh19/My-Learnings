# https://leetcode.com/problems/number-of-equivalent-domino-pairs/
class Solution:
    def numEquivDominoPairs(self, do: List[List[int]]) -> int:
        di = {}

        for i in range(len(do)):
            do[i].sort()
            t = tuple(do[i])
            if t not in di:
                di[t] = 1
            else:
                di[t] += 1

        
        ans = 0
        for k,v in di.items():
            ans += (v*(v-1))//2
                    
        return ans
                    