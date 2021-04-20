public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public int maxSubArray(final List<Integer> A) {
        int c =A.get(0);
        int b = A.get(0);
        
        for(int i=1;i<A.size();i++){
            
            if (A.get(i)> c + A.get(i)){
                c = A.get(i);
            }
            else{
                c+= A.get(i);
            }
            if (c > b){
                b = c;
            }
        }
        return b;
        
    }
}
