import java.util.*;
    
    public class GcdAndLcm{
    
    public static void main(String[] args) {
      // write your code here  
      
      Scanner in = new Scanner(System.in);
      int a = in.nextInt();
      int b = in.nextInt();
      
      int temp1 = a;
      int temp2 = b;
      while(b!=0){
        int n= b;
        
        b = a%b;
        a = n;
      }
      int gcd = a;
      int lcm = (temp1*temp2)/gcd;
      // a*b = lcm(a,b) * gcd(a,b)
      
      
      System.out.println("GCD is"+gcd);
      System.out.println("LCM IS "+lcm);
      
      in.close();
     }
    }