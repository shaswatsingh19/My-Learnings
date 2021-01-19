import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args) {
        int first = 0;
        int second = 1;
        int n = 2;
        Scanner in = new Scanner(System.in);
        int temp=0;
        int num = in.nextInt();
        System.out.print("0 , 1");
        while (n<num){
            temp=second;
            second = first + second;
            first = temp;
            System.out.print(" , " +second);
            n+=1;

        }
        in.close();
    }
}
