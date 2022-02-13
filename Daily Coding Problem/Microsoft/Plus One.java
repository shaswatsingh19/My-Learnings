// https://leetcode.com/problems/plus-one/
class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        int [] b = new int [n];
        int carry = 1;
        for (int i= n-1;i>-1;i--){
            b[i] = digits[i] + carry;
            if (b[i] > 9){
                carry = 1;
                b[i] = 0;
            }
            else{
                carry = 0;
            }
        }
        if (carry == 1 && b[0] == 0){
            int [] ne = new int [b.length+1];
            ne[0] = carry;
            ne[1] = b[0];
            for(int j= 2;j<ne.length;j++){
                ne[j] = b[j-1];
            }
            return ne;
        }
        return b;
        
    }
}