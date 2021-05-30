//https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
class Solution {
    public int minPairSum(int[] nums) {
        int n = nums.length;
        int start = n/2 -1;
        int end = n/2;
        int val = 0;
        Arrays.sort(nums);
        while(start>-1){
            val = Math.max(val,nums[start]+nums[end]);
            start--;
            end++;
        }
        return val;
        
    }
}