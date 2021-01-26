import java.util.Scanner;


// Series :1+ (1/2)+(1/3) + (1/4)+ ... + (1/n)

public class Series1 {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        float n = in.nextFloat();

        float a = 1.0f;

        for (float b = 2f ;b<=n;b++){
            a = a + (1/b);
        }
        System.out.println(a);
        
    in.close();
    } 
}
