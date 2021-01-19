public class FindBinary {
    public static void main(String[] args) {
        int num =7;
        String res="";
        int rem = 0;
        while (num!=0){
            rem = num % 2;
            num = num / 2;
            res = rem + res;

        }
        System.out.println(res);
    }
}
