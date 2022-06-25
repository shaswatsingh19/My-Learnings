# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.size = 0
        
    def push(self, val: int) -> None:
        if self.size == 0:
            self.minstack.append(val)    
                       
        elif val <= self.minstack[-1]:
            self.minstack.append(val)
        
        self.stack.append(val)
        self.size += 1

    def pop(self) -> None:
        if self.stack[-1] == self.minstack[-1]:
            self.minstack.pop() 
        self.stack.pop()
        
        self.size -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
            
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()