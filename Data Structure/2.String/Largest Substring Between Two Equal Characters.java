// 1624. Largest Substring Between Two Equal Characters
class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        
        int n = s.length()-1;
        int max= -1;
        for(int i=0;i<s.length();i++){
            char c = s.charAt(i);
            for(int j=n;j>i;j--){
                char ch = s.charAt(j);
                if (c==ch){
                    max = Math.max(max,(j-i-1));
                    break;
                }
                
            }
        }
        
        return max;
    }
}