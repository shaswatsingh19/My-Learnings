class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        s = 0
        for i in range(n):
            for j in range(i,n):
                if (j-i)%2==0:
                    s+=sum(arr[i:j+1])
        return s
        