abstract class Animal1{
    abstract void makeSound();
    
    
    static void legs(){
        System.out.println("animal classfour legs");

        
    }
}


class Dog1 extends Animal1{
    void makeSound(){
        System.out.println("BARK");
    }
}

class Cat1 extends Animal1{
    void makeSound(){
        System.out.println("MEOW");
    }
}

public class Abstraction {
    public static void main(String[] args) {
        Dog1 obj1 = new Dog1();

        obj1.makeSound();

        Cat1 obj2 = new Cat1();

        obj2.makeSound();

        Animal1.legs(); // we can't create objects of abstract class but can create abstract method and call it direct as static doesn't require you to make objects of it
        
    }
}
