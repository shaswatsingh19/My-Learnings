// https://leetcode.com/problems/single-number
class Solution {
    public int singleNumber(int[] nums) {
        int ans = 0;
        for(int i:nums){
            ans = ans ^ i;
        }
        return ans;
        // used bit manipulation as xor of two same is 0.
    }
}