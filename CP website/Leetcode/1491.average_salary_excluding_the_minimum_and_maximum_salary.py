# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution:
    def average(self, salary: List[int]) -> float:
        
        
        salary.sort()
        
        n  = len(salary)
        avg = sum(salary[1:-1])
        return avg/(n-2)