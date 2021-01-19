public class SwapWithBit {
    public static void main(String[] args) {
        // we use xor to swap without using temp variable
        int a = 5;
        int b  = 6;

        a = a ^ b;
        System.out.println(a+" "+b);
        b = a ^ b;
        System.out.println(a+" "+b);
        a = a ^ b;
        System.out.println(a+" "+b);
    }
}
