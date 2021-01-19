public class PrimeOrNot {
    public static void main(String[] args) {
        long n = 1999991312;
        boolean flag  = true;
        for (int i=2 ; i*i<n ; i++){
            if (n%i==0){
                flag = false;
                break;
            }
        }
        if (flag==false || n==1){
            
            System.out.println("NOT PRIME");
        }
        else{
            System.out.println("PRIME");
        }
    }
}
