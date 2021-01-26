public class SetithBit {
    public static void main(String[] args) {
        int num = 8;
        // for setting ith bit we simply do OR operation with 1<<(ith time)
        // 1000 | (1<<2) after setting we have 1100
        System.out.println("WE want to set 2 bit");
        int i = 2;
        int check = 1<<2;
        num = num | check;
        System.out.println(num);
    }
}
