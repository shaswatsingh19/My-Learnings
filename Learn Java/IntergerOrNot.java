import java.util.Scanner;

public class IntergerOrNot{
    public static void main(String args[]){
        Scanner in = new Scanner(System.in);

        boolean a = in.hasNextInt();
        System.out.println(a);
        
    in.close();
    }
}