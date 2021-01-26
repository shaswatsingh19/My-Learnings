import java.util.Scanner;
public class KmToMiles {

    public static void main(String args[]){
        Scanner inp = new Scanner(System.in);
        float km = inp.nextFloat();

        float mile = km*0.621f;

        System.out.println(mile);

        inp.close();
    }
    
}
