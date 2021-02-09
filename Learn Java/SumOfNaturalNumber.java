import java.util.Scanner;

public class SumOfNaturalNumber {

    int sum(int n){
        if (n==1) return 1;
        else{
            return (n+sum(n-1));
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        SumOfNaturalNumber obj = new SumOfNaturalNumber();
        System.out.println(obj.sum(n));
        in.close();
    }    
}
