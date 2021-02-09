public class PatterUsingMethod1 {


    static void pattern(int n){
        for (int i = 1;i<=n;i++){
            for (int j=0;j<i;j++){
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
