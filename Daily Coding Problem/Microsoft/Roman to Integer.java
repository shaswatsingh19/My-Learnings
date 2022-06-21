// https://leetcode.com/problems/roman-to-integer/
class Solution {
    public int romanToInt(String s) {
        Map<Character,Integer> map = new HashMap<>();
        map.put('I',1);
        map.put('V',5);
        map.put('X',10);
        map.put('L',50);
        map.put('C',100);
        map.put('D',500);
        map.put('M',1000);
        int ans = 0;
        char [] ch = s.toCharArray();
        int n = ch.length;
        ans += map.get((ch[n-1]));
        for(int i=n-2;i>-1;i--){
            int val =  map.get((ch[i]));
            if (map.get(ch[i+1]) > map.get(ch[i])){
                ans -= val;
            }
            else{
                ans +=val;
            }
        }
        return ans;
    }
}