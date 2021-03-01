interface Polygon1{
    void getArea();

    default void getPerimeter(int ...sides){
        int perimeter=0;
        for (int side :sides) perimeter += side;

        System.out.println("perimeter is "+perimeter);
    }
}

class Rectangle1 implements Polygon1{
    private int a,b;
    private int area;

    Rectangle1(int a,int b){
        this.a=a;
        this.b =b;
    }

    public void getArea(){

        area = a*b; 
        System.out.println("AREA IS "+area);
    }
}

public class InterfaceExample {
    public static void main(String[] args) {
        Rectangle1 obj = new Rectangle1(3,6);

        obj.getArea();
        obj.getPerimeter(3,6);

    }
}
