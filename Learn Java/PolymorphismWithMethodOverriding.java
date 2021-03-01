class Car{
    void show(){
        System.out.println("THIS IS CAR");
    }
}

class Bmw extends Car{
    @Override
    public void show(){
        System.out.println(" THIS IS BMW CAR");
    }
}

public class PolymorphismWithMethodOverriding {
    public static void main(String[] args) {
        Bmw obj = new Bmw();
        obj.show(); // ThIS IS BMW CAR as it overrides it.
    }
}
