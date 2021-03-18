import java.util.*;

public class ReverseANumber {

    public static void main(String[] args) {
    
    Scanner in = new Scanner(System.in);

    int n = in.nextInt();int reversed = 0;
    while(n>0){
        int last = n%10;
        System.out.println(last);
        reversed = reversed*10 + last;
        n/=10;
    }
    
    System.out.println(reversed);


    in.close();

    }
   }

