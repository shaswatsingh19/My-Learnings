class Solution:
    def largestOddNumber(self, num: str) -> str:
        n = len(num)
        for i in range(n-1,-1,-1):
            # print(num[i])
            if(int(num[i])%2 != 0):
                # print(num[:i+1])
                return num[:i+1]
        return ""