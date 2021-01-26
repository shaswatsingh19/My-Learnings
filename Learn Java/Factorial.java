import java.util.Scanner;

public class Factorial {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int fact = 1;
        int num = in.nextInt();
        for (int i=num;i>1;i--){
            fact *= i;
        }
        System.out.println(fact);
        in.close();
    }
}
