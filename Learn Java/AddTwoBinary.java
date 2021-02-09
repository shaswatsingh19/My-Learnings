import java.util.Scanner;
public class AddTwoBinary {

    int addTwoBin(int a,int b){
        // making an obj of binary to decimal class and use it method to find bintodec()
        BinaryToDecimal obj1 = new BinaryToDecimal();
        int ans = obj1.binToDec(a)+obj1.binToDec(b);
        System.out.println("The decimal value is "+ans);
        //    make a obj to deciaml to binary class and use it method to convert dec to binary
        DecimalToBinary obj2 = new DecimalToBinary();
        int res = obj2.decToBin(ans);
        return res;
    }
    


    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        AddTwoBinary obj = new AddTwoBinary();
        System.out.print("Enter first binary");
        int a = in.nextInt();
        
        System.out.print("Enter Second binary");
        int b = in.nextInt();

        int res = obj.addTwoBin(a, b);
        // now  res is a decimal number for converting into binary we send to decimal to binary class
      
    
        System.out.println("THE BINARY after adding "+a +" and "+b+" is"+res);
        

        in.close();
    }
}
