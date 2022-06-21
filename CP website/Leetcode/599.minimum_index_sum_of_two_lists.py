# https://leetcode.com/problems/minimum-index-sum-of-two-lists/
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        di = {}
        l = len(list1)
        
        mini = 99999999
        for i in range(l):
            if list1[i] in list2:
                di[list1[i]] = i + list2.index(list1[i])
                mini = min(mini,di[list1[i]])
        
                
        for k,v in di.items():
            if v==mini:
                list1.append(k)
                
        return list1[l:]
                
        