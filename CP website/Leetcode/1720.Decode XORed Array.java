//https://leetcode.com/problems/decode-xored-array
class Solution {
    public int[] decode(int[] encoded, int first) {
        int l = encoded.length;
        int arr[] = new int[l+1];
        arr[0] =  first;
        for(int i=1;i<l+1;i++){
            arr[i] = arr[i-1] ^ encoded[i-1];
        }
        
        
        
        
        return arr;
    }
}