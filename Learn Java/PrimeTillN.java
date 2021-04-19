
import java.util.Scanner;

public class PrimeTillN {
    static void prime(int num){
        
        int [] arr = new int[num+1];
        for (int i = 2; i < arr.length; i++) {
            arr[i]=1;
        }

        for (int i = 2; i*i <= num; i++) {
            if (arr[i]==1){
                for (int j = i*i; j <= num; j+=i) {
                    arr[j] = 0;                    
                }
            }
        }

        
        
        
        int x = 2;
        while(x<arr.length){
            if(arr[x] == 1 && num%x==0){
                    num = num/ x;
                    System.out.println(x);
                    x--;
                }
            if(num<=1)break;
            x++;
        }       
        
    }
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        prime(num);
        in.close();
    } 
}
