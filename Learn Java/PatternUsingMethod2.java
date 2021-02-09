public class PatternUsingMethod2 {


    static void pattern(int n){
        for (int i = 1;i<=n;i++){
            for (int j=i;j<=n;j++){
                System.out.print(" x ");
            }
            System.out.println();
        }

    }
    public static void main(String[] args) {
        int n =4;
        pattern(n);
    }
}
