import java.util.Scanner;

public class DecimalToHex {

    void decToHex(int dec){//26

        DecimalToBinary obj1 = new DecimalToBinary();
        
        int bin = obj1.decToBin(dec);

        System.out.println("Binary of "+dec+" is:"+bin);//0001 1010
        String ans = " ";
        while(bin>0){
            int rem = bin%10000; //rem  = 1010
            BinaryToDecimal obj2 = new BinaryToDecimal();
            int new_dec = obj2.binToDec(rem); // new_dec = 10
            switch(new_dec){
                case 10:ans = "A"+ans; // ans = "A"+" "
                break;
                case 11:ans = "B"+ans;
                break;
                case 12:ans = "C"+ans;
                break;
                case 13:ans = "D"+ans;
                break;
                case 14:ans = "E"+ans;
                break;
                case 15:ans = "F"+ans;
                break;
                default:ans= new_dec + ans;// ans = 1 + "A"
           
            }
            bin = bin / 10000;// bin = 1
        }
        System.out.println("Hexadecimal value of "+dec+" is:" +ans);
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int dec = in.nextInt();//26

        DecimalToHex obj = new DecimalToHex();
        obj.decToHex(dec);

        in.close();

    }
}
