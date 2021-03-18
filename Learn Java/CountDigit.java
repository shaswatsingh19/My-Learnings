import java.util.*;
  
public class CountDigit {

  public int countDigit(int n){
    int cnt=0;
while(n>0){
    n = n/10;
    cnt++;
}
return cnt;
}

  
  public static void main(String[] args) {
    
    Scanner in = new Scanner(System.in);
    
    int n = in.nextInt();//25

    CountDigit obj  = new CountDigit();
    int cnt = obj.countDigit(n);
    System.out.println(cnt);
    
    

  }
  }

