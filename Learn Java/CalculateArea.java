class Square{
    int side;

    int area(){
        return side*side;
    }

    int perimeter(){
        return 4*side;
    }
}

public class CalculateArea {
    public static void main(String[] args) {
        Square obj = new Square();

        obj.side = 7;
        System.out.println("Areas is "+obj.area());
        System.out.println("Perimeter is "+obj.perimeter());
        

    }
}
