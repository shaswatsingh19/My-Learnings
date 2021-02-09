import java.util.Scanner;


public class TableOfNUsingMethod {

    void tableOfN(int n){

        for (int i = 1; i<=10;i++){
            System.out.println(n+" X "+i+" = " +n*i);
        }
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        TableOfNUsingMethod obj = new TableOfNUsingMethod();
        int n = in.nextInt();
        obj.tableOfN(n);


        in.close();
    }
}
