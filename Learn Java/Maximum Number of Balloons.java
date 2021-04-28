//https://leetcode.com/problems/maximum-number-of-balloons/
class Solution {
    public int maxNumberOfBalloons(String text) {
        char [] ch = text.toCharArray();
        
        int b = 0;
        int a = 0;
        int l = 0;
        int o = 0;
        int n = 0;
        int cnt=0;
        for(char c :ch){
            if (c=='b') b+=1;
            else if (c=='a') a+=1;
            else if (c=='l') l +=1;
            else if (c=='o') o += 1;
            else if (c =='n') n+=1;
            if ((b>0) && (a>0) && (l>1) && (o>1) && (n>0)){
                cnt+=1;
                b-=1;
                a-=1;
                l-=2;
                o-=2;
                n-=1;
            }
        }
        
        
        return cnt;
    }
}