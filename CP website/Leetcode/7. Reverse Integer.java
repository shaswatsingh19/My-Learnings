//https://leetcode.com/problems/reverse-integer/
class Solution{
    public int reverse(int x) {
        boolean pos = x > 0;
        x = Math.abs(x);
        // String s =  "";
        int temp = 0;
        int ans = 0;

        while(x >0){
            int rem = x % 10;
            
            if( ans > Integer.MAX_VALUE/10 || (ans== Integer.MAX_VALUE && rem > 7)){
                return 0;
            }
            if (ans < Integer.MIN_VALUE/10 || (ans == Integer.MIN_VALUE && rem < - 8)){
                return 0;
            }
            x = x / 10;
            temp = ans * 10 + rem;
            ans = temp ;
        }
        return (pos ? ans : ans*-1);
    }
}