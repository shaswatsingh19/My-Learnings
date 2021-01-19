import java.util.Scanner;

class Marks{
    public static void main(String args[]){
        Scanner inp = new Scanner(System.in);

        float m1 = inp.nextFloat();
        float m2 = inp.nextFloat();
        float m3 = inp.nextFloat();
        
        float per = ((m1+m2+m3))/3;

        System.out.println(per);
        
    inp.close();
    }
}