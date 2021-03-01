class Add1{
    void add(int a,int b){
        System.out.println(a+b);
    }

    void add(String a,String b){
        System.out.println(a+" "+b);
    }
}

public class PolymorphismwithOperatorOverloading {
    public static void main(String[] args) {
        Add1 obj = new Add1();

        obj.add(1,2);

        obj.add("java","program");
    }
}
