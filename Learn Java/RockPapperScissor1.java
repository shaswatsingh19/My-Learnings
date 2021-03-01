import java.util.Random;
import java.util.Scanner;

public class RockPapperScissor1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Choose between 0,1,2");

        int userInp = in.nextInt();
        Random rand = new Random();
        
        int compInp = rand.nextInt(3);
        System.out.println(compInp);

        String res = "";
        if (userInp == compInp) res ="draw";
        else if (userInp==0){
            if (compInp==1) res= "computer win";
            else res="user wins";
        }
        else if (userInp==1){
            if (compInp==0) res= "computer win";
            else res="user wins";
        }
        else{
            if (compInp==0) res= "computer win";
            else res="user wins";
        }
        System.out.println(res);
     
        in.close();

    }
}
