import java.util.*;
    
public class DigitOfANumber {

    
    public static void main(String[] args) {
      // write your code here  
      Scanner in = new Scanner(System.in);

      String str =in.next();
      char []ch = str.toCharArray();
      
      for (char c : ch) {
          System.out.println(c);
      }


      in.close();
      
      
     }
    }
