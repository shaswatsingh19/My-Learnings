# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.size = 0
        

    def push(self, x: int) -> None:
        self.stack1.append(x)
        self.size += 1

    def pop(self) -> int:
        while len(self.stack1) > 1:
            self.stack2.append(self.stack1.pop())
            
        val = self.stack1.pop()
        self.size -= 1
        
        # self.stack2.reverse()
        # self.stack1 = self.stack2.copy()
        
        while len(self.stack2) > 0:
            self.stack1.append(self.stack2.pop())
        
        return val
        

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.size == 0:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()