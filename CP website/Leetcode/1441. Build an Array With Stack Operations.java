class Solution {
    public List<String> buildArray(int[] target, int n) {
        
        
        List<String> list = new ArrayList<>();
        int max = 0;
        for(int i=0;i<target.length;i++){
            if (target[i]>max){max = target[i];}
        }
        
        int i =1;
        int j =0;
        while(i<=n && i<=max){
            if(target[j] == i){
                list.add("Push");
                i++;
                j++;
            }
            else{
                list.add("Push");
                list.add("Pop");
                i++;
            }
        }
        return list;
    }
}