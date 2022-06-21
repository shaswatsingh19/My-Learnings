// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/
class Solution {
    public int countGoodSubstrings(String s) {
         int end = 3;
        int n = s.length();
        int cnt = 0;
        if(n<3){
            return 0;
        }
        for(int  i = 0;i<=n-3;i++){
            String s1 = s.substring(i,end);
            end++;
            // System.out.println(s1);
            int m = s1.length();
            HashSet<Character> set = new HashSet<>();
            for(int j = 0;j<m;j++){
                char c = s1.charAt(j);
                set.add(c);
            }
            // System.out.println(set);

            if(set.size() == m){
                cnt+=1;
            }
        }
        // System.out.println(cnt);
        return cnt;
    }
}