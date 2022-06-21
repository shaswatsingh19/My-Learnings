class Solution {
    public int pivotIndex(int[] nums) {
        int sum = 0;
        for(int i : nums){
            sum+=i;
        }
        int eft = 0;
        for(int i =0 ;i<nums.length;i++){
            if(eft == sum - eft - nums[i]){
                return i;
            }
            eft+=nums[i];
        }
    
    return -1;
    }
}