//https://leetcode.com/problems/binary-search/
class Solution {
    public int search(int[] nums, int target) {
        
        int s = 0;
        int e = nums.length-1;
        return binary(nums,target,s,e);
        
    }
    
    public static int binary(int nums[] , int target,int s,int e){
        int mid = s + (e-s)/2;
        while(s<=e)
        {if(nums[mid] == target){
            return mid;
        }
        else if(nums[mid]<target){
            s  = mid+1;
            return binary(nums,target,s,e);
        }
        else{
            e = mid-1;
            return binary(nums,target,s,e);
        }}
        return -1;
    }
}