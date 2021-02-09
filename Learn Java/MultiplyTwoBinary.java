import java.util.Scanner;

public class MultiplyTwoBinary {

    void multiTwoBin(int a,int b){

        BinaryToDecimal obj1 = new BinaryToDecimal();
        int dec_a_b = obj1.binToDec(a) * obj1.binToDec(b);

        System.out.println("First binary value is "+a);
        System.out.println("Deciaml value of "+a+" is "+obj1.binToDec(a));
        
        System.out.println("Second binary value is "+b);
        System.out.println("Deciaml value of "+b+" is "+obj1.binToDec(b));

        System.out.println("multiplication of "+a+" and "+b+" is "+dec_a_b);

        DecimalToBinary obj2 = new DecimalToBinary();
        int bin_a_b = obj2.decToBin(dec_a_b);

        System.out.println("Binary of "+dec_a_b +" is "+bin_a_b);

        
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("ENTER two binary number");
        int a = in.nextInt();//11
        int b = in.nextInt();//10

        MultiplyTwoBinary obj  = new MultiplyTwoBinary();
        obj.multiTwoBin(a, b);






        in.close();
    }   
}
