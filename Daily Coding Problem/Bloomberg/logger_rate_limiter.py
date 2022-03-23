# https://leetcode.com/problems/logger-rate-limiter/
class Logger:

    def __init__(self):
        self.di = {}
        

    def shouldPrintMessage(self, t: int, m: str) -> bool:
        if m not in self.di:
            self.di[m] = t
            return True
        else:
            if t - self.di[m] >=10:
                self.di[m] = t
                return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)