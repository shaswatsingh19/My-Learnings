class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        int cnt = 0;
        for (int i=0;i<nums1.length;i++){
            boolean ispresent = false;
            for(int j=0;j<nums2.length;j++){
                if(nums1[i] == nums2[j]){
                    nums2[j] = -1;
                    ispresent = true;
                    break;
                }
            }
            if(!ispresent){
              nums1[i] = -1;
                cnt+=1;
            }
        }
        int [] arr = new int[nums1.length-cnt];
        int k = 0;
        for(int i=0;i<nums1.length;i++){
            if(nums1[i] != -1){
                arr[k++] =  nums1[i];
                
            }
        }
        
        return  arr;
    }
}