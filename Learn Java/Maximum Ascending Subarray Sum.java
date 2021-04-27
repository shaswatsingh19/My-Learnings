class Solution {
    public int maxAscendingSum(int[] nums) {
        int max = nums[0];
        int temp =nums[0];
        
        for(int i=1;i<nums.length;i++){
            if (nums[i]>nums[i-1]){
                temp += nums[i];
            }
            else{
                temp = nums[i];
            }
            max = Math.max(temp,max);
        }
        return max;
    }
}