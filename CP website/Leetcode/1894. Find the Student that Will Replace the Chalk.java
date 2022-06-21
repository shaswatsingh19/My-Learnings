class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int i=0;
        int n=chalk.length;
        int add=0;
        for(int j=0;j<n;j++){
            add+=chalk[j];
            if(add>k){
                return j;
            }
        }
        k=k%add;
        
        while(chalk[i%n]<=k){
            k-=chalk[i%n];
            i++;
        }
        return i%n;
    }
}