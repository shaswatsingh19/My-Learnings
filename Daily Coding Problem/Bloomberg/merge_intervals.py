# https://leetcode.com/problems/merge-intervals/
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        
        ans  = []
        
        intervals.sort()
        
        ans.append(intervals[0])
        
        i = 1
        
        while i<len(intervals):
            curr = intervals[i]
            
            
            if (curr[0] <= ans[-1][1]):
                ans[-1] = [ ans[-1][0] , max( curr[1], ans[-1][1] ) ]
                
            else:
                ans.append(curr)
                
            i+=1
            
        return ans