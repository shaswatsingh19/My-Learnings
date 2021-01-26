public class NoOfBitInAandB {
    public static void main(String[] args) {
        // Find the number of bit we have to change to get from a to b
    // a = 10110 
    // b = 11011 so we can see we have to change 0,2 and 3 bit from a to make it to b
    // solution :
    // XOR (a and b) and check for odd value but right shifing  result & with 1
    int a = 22;
    int b = 27;
    int res = a^b;
    int check=0;
    int count = 0;
    while (res != 0){
        
        check = res & 1;
        if (check == 1){
            count +=1;
        }
        res = res >> 1;
    }
    System.out.println("We have to change "+count+" bit to make "+a+" is equal to "+b);

    }
}
