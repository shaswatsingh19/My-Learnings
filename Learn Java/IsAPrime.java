import java.util.*;
  
  public class IsAPrime{
  
  public static void main(String[] args) {
      Scanner scn = new Scanner(System.in);
  
       // write ur code here
       int  t = scn.nextInt();
       while(t>0){
           int n = scn.nextInt();
           String ans = "prime";
           for(int i =2;i*i<=n;i++){
               if (n%i==0){
                   ans= "not prime";
                   break;
               }
           }
           System.out.println(ans);

           t--;
       }
  
   }
  }