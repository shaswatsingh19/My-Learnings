/*
* * * *
  * * *
    * *
      *
*/
public class Patterns3 {
    public static void main(String[] args) {
        int n = 4;
        for  ( int i = n ; i>=1;i--){
            for (int k = i;k<n;k++){
                System.out.print("  ");
            }
            for (int j = 0;j<i;j++){
                System.out.print(" *");

            }
            System.out.println( );
        }
    }
}