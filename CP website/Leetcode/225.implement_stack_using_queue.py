class Solution {
    public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0# https://leetcode.com/problems/implement-stack-using-queues
class MyStack:
    def __init__(self):
        # using 2 queue
        self.q1 = []
        self.q2 = []
        self.size = 0     

    def push(self, x: int) -> None:
        self.q1.append(x)
        self.size += 1
        return
        
        

    def pop(self) -> int:
        temp = self.size 
        while  temp > 1:
            self.q2.append(self.q1.pop(0))
            temp -= 1
        
        self.q1, self.q2 = self.q2,self.q1
        self.size -= 1
        return self.q2.pop()
        

    def top(self) -> int:
        return self.q1[-1]
        

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty(); i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}
}