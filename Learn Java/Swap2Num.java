public class Swap2Num {
    public static void main(String[] args) {
        int first = 2;
        int second = 5;
// temp = 2
// first = 5
        System.out.println("Intial value of first is"+first+" and second is "+second);
        int temp;
        temp = first;
        first = second;
        second = temp;

        System.out.println("After Swap");
        
        System.out.println("Intial value of first is"+first+" and second is "+second);


    }
}
