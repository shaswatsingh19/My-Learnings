# https://leetcode.com/problems/kth-largest-element-in-a-stream/
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.karr = []
        self.k = k
        nums.sort(reverse = True)
        i=0
        while i<len(nums):
            self.karr.append(nums[i])
            i+=1
        i=0
        while len(self.karr)>k:
            self.karr.pop()

    def add(self, val: int) -> int:
        
        self.karr.append(val)
        if len(self.karr)>self.k:
            self.karr.sort(reverse = True)
            self.karr.pop()
            self.largest = self.karr[-1]
            return self.largest
        
        self.karr.sort(reverse = True)
        self.largest = self.karr[-1]
            
        return self.largest
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)