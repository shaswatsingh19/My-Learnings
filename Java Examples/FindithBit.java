import java.util.Scanner;

public class FindithBit {
    public static void main(String[] args) {
        /**
         To find ith bit we first do num>>(i-1) times and perform 
         and operation (&) if result == 1 means ith bit is 1
         else 0
         */
        
        Scanner in = new Scanner(System.in);
        int num = 13;
        System.out.print("Which bit would you like to find: ");
        int i = in.nextInt();

        int n = num>>(i-1);

        int check = n & 1 ;
        if (check==0){
            System.out.println(i+"th bit is 0");
        }else System.out.println(i+"th bit is 1");




        in.close();
    }
}
