# https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        for i in boxTypes:
            i[0],i[1] = i[1],i[0]
            
            
        boxTypes.sort(reverse=True)
        
        ans = 0
        truckCap = 0
        for i in boxTypes:
            truckCap += i[1]
            if truckCap < truckSize:
                ans += i[0]*i[1]
            else:
                truckCap -= i[1]
                rem = truckSize - truckCap
                ans += i[0]*rem
                break
                
        return ans
            