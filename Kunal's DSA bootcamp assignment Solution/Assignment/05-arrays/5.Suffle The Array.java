// https://leetcode.com/problems/shuffle-the-array
class Solution {
    public int[] shuffle(int[] nums, int n) {
        int [] ans  = new int[n*2];
        int j=0;
        for(int i=0;i<n;i+=1){
            ans[j] = nums[i];
            ans[j+1] = nums[n+i];
            j+=2;
        }
        return ans;
    }
}
