public class FibonacciUsingRecursion {

    int fibRecur(int n){
        if (n==0) return 0;
        else if (n==1) return 1;
        else {
            return (fibRecur(n-1) + fibRecur(n-2));
        }
    }
    public static void main(String[] args) {
        FibonacciUsingRecursion obj = new FibonacciUsingRecursion();
        int n = 1;
        System.out.println(obj.fibRecur(n));
    }
}
