// Find unique element from the array where each element occur k times
// with O(n) time and space 
// we can also do with hashset 
public class FindElement3 {

    public static void findElement3(int []arr,int n,int k) {

        int [] count = {0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,
                        0,0,0,0,0,0,0,0,0,0,0,0};
        for (int i:arr){
            int c =0;
            int temp=i;//4 = 100
            while(c<32){
                if((temp&1)==1){
                    count[c]+=1;
                }
                temp = temp>>1;
                c+=1;
            }
        }

        double ans = 0;
        int j =0;
        for (int i:count){
            int rem = i%k;
            ans = ans + (1<<j)*rem;
            j+=1;

        }
        System.out.println((int)ans);
    }
    public static void main(String[] args) {
        int [] arr = {1,1,1,2,2,2,3,4,4,4};
        int n = arr.length;
        int k=3;
        findElement3(arr,n,k);
    }
    
}
