import java.util.Scanner;

public class Input{

    public static void main(String args[]){
        System.out.println("SDASD");

        Scanner inp = new Scanner(System.in);

        int a = inp.nextInt();
        System.out.println(a+100);
        String b = inp.next();
        System.out.println(b+"world");
        // .next() would take only one word
        String name = inp.next();
        
        System.out.println(name);
        //.nextline() take full sentence
        String fullName = inp.nextLine();

        
        System.out.println(fullName);
        inp.close();
    }

}