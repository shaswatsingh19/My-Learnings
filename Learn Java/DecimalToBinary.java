import java.util.Scanner;

public class DecimalToBinary {

    int decToBin(int num){
        String res="";
        int rem = 0;
        while (num!=0){ 
            rem = num % 2;
            num = num / 2;
            res = rem + res;

        }
        return Integer.parseInt(res);

    }
    public static void main(String[] args) {
         Scanner in = new Scanner(System.in);
         int num = in.nextInt();
        DecimalToBinary obj = new DecimalToBinary();

        System.out.println(obj.decToBin(num));
        in.close();
    }
}
