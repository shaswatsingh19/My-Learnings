public class ClearithBit {
    public static void main(String[] args) {
        int num = 15;
        // for clearning the ith bit just perform XOR with (1<<i)

        System.out.println("Clear the 3 bit");
        int i = 1<<3;
        num = num ^ i;
        System.out.println(num);
        // 1111 will converted to 0111 as 3rd bit is clear
    }
}
