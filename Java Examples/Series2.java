import java.util.Scanner;


// Series :1 - (1/2) + (1/3) - (1/4)+ (1/5) - (1/6)... + (1/n)

public class Series2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
    
        float n = 3f;
    
        float result = 1.0f;
    
        for (float i=2f;i<=n;i++){
            if (i % 2==0) i = (-1)*i;
            result = result + (1/i); 
    
        }
        System.out.println(result);
        in.close();
    }
}
