import java.util.Scanner;
public class BinaryToDecimal {
    
    int binToDec(int n){

        
        int ans = 0;
        int last_digit=0;
        int base = 1;  // as 2^0 = 1
        while (n>0){
            last_digit = n % 10;
            ans += last_digit*base;
            base *= 2;
            n /= 10;
        }
        return ans;

    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        BinaryToDecimal obj = new BinaryToDecimal();
        int bin = in.nextInt();
        //110
        int ans = obj.binToDec(bin);
        System.out.println(ans);
        in.close();
    }    
}
