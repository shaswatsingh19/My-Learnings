// https://leetcode.com/problems/longest-common-prefix/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Map<String,Integer> map = new HashMap<>();
        for (int i=0;i<strs.length;i++){
            String s = strs[i];
            int n = s.length();
            for(int j=0;j<s.length();j++){
                String sub = s.substring(0,j+1);
                if(map.containsKey(sub)){
                    map.put(sub,map.get(sub)+1);
                }
                else{
                    map.put(sub,1);
                }
            }
        }
                        System.out.println(map);
        int lenk = 0;
        int val = 0;
        String newKey = "";
        for(String key : map.keySet()){
            if(map.get(key) > val){
                val = map.get(key);
                newKey = key;
            }
            if(map.get(key) == val && key.length() > newKey.length()){
                newKey = key;
            }
        }
        if(map.getOrDefault(newKey,0) == strs.length){
            return newKey;
        }
        return "";
        
    }
}class Solution {
    public String longestCommonPrefix(String[] strs) {
        Map<String,Integer> map = new HashMap<>();
        for (int i=0;i<strs.length;i++){
            String s = strs[i];
            int n = s.length();
            for(int j=0;j<s.length();j++){
                String sub = s.substring(0,j+1);
                if(map.containsKey(sub)){
                    map.put(sub,map.get(sub)+1);
                }
                else{
                    map.put(sub,1);
                }
            }
        }
                        System.out.println(map);
        int lenk = 0;
        int val = 0;
        String newKey = "";
        for(String key : map.keySet()){
            if(map.get(key) > val){
                val = map.get(key);
                newKey = key;
            }
            if(map.get(key) == val && key.length() > newKey.length()){
                newKey = key;
            }
        }
        if(map.getOrDefault(newKey,0) == strs.length){
            return newKey;
        }
        return "";
        
    }
}