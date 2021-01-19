import java.util.Scanner;

public class XpowerY {
    public static void main(String[] args) 
    {
        Scanner in = new Scanner(System.in);

        System.out.print("Enter value of X(base) :");
        int x = in.nextInt();
        System.out.print("Enter value of Y(power) :");
        int y = in.nextInt();
        
        int temp=1;
        for (int i =0;i<y;i++){
            temp = x*temp;
        }

        System.out.println(x+" raised to the power of "+y+" is "+temp);
        in.close();

    }
}
