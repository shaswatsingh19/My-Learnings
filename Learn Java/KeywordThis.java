class Main1{
    int var;

    Main1(int var){
        this.var = var;
        System.out.println("this referecne "+ this);
    }

}
public class KeywordThis {
    public static void main(String[] args) {
        Main1 obj = new Main1(9);

        System.out.println("object reference "+obj);
        /*
        Output is :=>
        this referecne Main1@6f75e721
        object reference Main1@6f75e721
        */


    }
}
