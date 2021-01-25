public class ReverseBits{
    public static void main(String[] args) {
        long a = 2;
        int c=0;
        long temp = a;
        while(temp!=0){
            c+=1;
            temp = temp>>1;
        }
        
        int right = 32 - c;
        System.out.println(right);

        System.out.println(a<<right);
    }
}