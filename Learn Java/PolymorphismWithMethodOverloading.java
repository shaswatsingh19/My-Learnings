class Polygon3{
    void side(){
        System.out.println("polygon has many side");
    }

    void side(int a,int b,int c){
        System.out.println("A TRIANGLE WITH sides "+a+" "+b+" "+c);
    }

    void side (int a,int b,int c,int d){
        System.out.println("A Quadilateral WITH sides "+a+" "+b+" "+c+" "+d);
    }
}


class PolymorphismWithMethodOverloading{
    public static void main(String[] args) {

        Polygon3 obj = new Polygon3();

        obj.side();

        obj.side(1,2,3);

        obj.side(2, 6, 12, 4);
        
    }
}