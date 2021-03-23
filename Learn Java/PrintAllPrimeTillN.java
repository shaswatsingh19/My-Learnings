import java.util.*;

public class PrintAllPrimeTillN {

    public static void main(String[] args) {
        // write your code here
        Scanner in = new Scanner(System.in);
        int n1 = in.nextInt();
        int n2 = in.nextInt();

        for (int i= n1;i<=n2;i++){
            boolean ans =true;
            for (int j=2;j*j<=i;j++){
                if(i%j==0){
                    ans = false;
                    break;
                }
            }
            if(ans){System.out.println(i);}

        }
        in.close();

    }
}

