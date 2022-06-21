// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
class Solution {
    public int subtractProductAndSum(int n) {
     
         int pro = 1;
        int s = 0;
        while(n>0){
            int rem = n%10;
            pro = pro * rem;
            s = s + rem;
            n = n/10;
            
        }
        return pro-s;
    }
}