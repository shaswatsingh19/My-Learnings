# https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage:

    def __init__(self, size: int):
        self.arr = []
        self.size = size
        

    def next(self, val: int) -> float:
        ans = 0
        if len(self.arr)>=self.size:
            el  = self.arr[0]
            self.arr.remove(el)
            return self.next(val)

        self.arr.append(val)
        s = sum(self.arr)
        l = len(self.arr)
        ans = s/l

        return ans
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)