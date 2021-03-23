import java.util.Arrays;
import java.util.Scanner;

class TheCuriousCaseOfBenjaminBulbs{
    public static void main(String[] args) {
        


        Scanner in = new Scanner(System.in);
        int n = in.nextInt();

        int []arr = new int[n];
        System.out.println(Arrays.toString(arr));
        for (int i = 0; i < arr.length; i++) {
            
            for (int j = 0; j < arr.length; j++) {
                if( (j+1) % (i+1)==0){
                    if(arr[j]==0) arr[j]=1;
                    else arr[j]=0;
                }
                
            }
        }



        for (int i = 0; i < arr.length; i++) {
            if(arr[i]==1) System.out.println(i+1);
        }
        in.close();
    }
}