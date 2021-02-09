import java.util.Arrays;
import java.util.Scanner;

public class ArrayLoop {
    public static void main(String[] args) {
        String [] arr = new String[10];
        Scanner in  = new Scanner(System.in);
        for (int i = 0;i<arr.length;i++){
            arr[i] = in.next();
        }

        for (int i = 0;i<arr.length;i++){
            System.out.print(arr[i]+" ");
        }

        System.out.println(Arrays.toString(arr));
        
        in.close();
    }
}
