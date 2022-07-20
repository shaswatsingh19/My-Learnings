# https://leetcode.com/problems/insert-interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        ans  = []
        
        i = 0
        while i<len(intervals):
            
            curr = intervals[i]
            
            if (curr[1] < newInterval[0]):
                # until the curr value is less then newInterval
                ans.append(curr)
            
            elif (curr[0] <= newInterval[1]):
                # can be merged 
                newInterval = [ min( curr[0] , newInterval[0] ) , max( curr[1],newInterval[1]) ]
                
            else:
                # when we didn't find the interval
                ans.append(newInterval)
                newInterval = curr
                
            i+=1
                
        ans.append(newInterval)
        
        return ans