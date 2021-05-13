// https://leetcode.com/problems/move-zeroes/submissions/
class Solution {
    public void moveZeroes(int[] nums) {
        
        int z = 0;
        for(int cur = 0;cur<nums.length;cur++){
            if(nums[cur]!= 0){
                int temp = nums[z];
                nums[z] = nums[cur];
                nums[cur] = temp;
                z++;
            }
        }
    }
}