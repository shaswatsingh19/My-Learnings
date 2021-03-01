// interface is also called fully abstract class
interface polygon{
    void area(int length,int width);
    // in interface every method is abstract 
}


class Rectangle implements polygon{

    public void area(int l,int b){
        System.out.println(l*b);
    }
}

public class Interface {
    /*
    Similar to class but provide multiple inheritance 
    class a implements class b , class c
    */
    public static void main(String[] args) {
        Rectangle obj = new Rectangle();

        obj.area(2,4);
        
    }
}


/*

interface Line {
…
}

interface Polygon {
…
}

class Rectangle implements Line, Polygon {
…
}

default methods in Java Interfaces
With the release of Java 8, we can now add methods with implementation inside an interface. These methods are called default methods.

To declare default methods inside interfaces, we use the default keyword. For example,

public default void getSides() {
   body of getSides()
}
 */