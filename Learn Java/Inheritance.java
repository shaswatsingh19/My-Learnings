class Animal{//superclass
    public String name;
    void eat(){
        System.out.println("I CAN EAT");
    }
    void display(){
        System.out.println("display of superclass");
    }
}

class Dog extends Animal{
    //subclass

    void display(){
        System.out.println("My name is "+name);
    }
}


class Inheritance{
    public static void main(String[] args) {

        Dog doberman = new Dog();
        doberman.name="rahul";// access field of superclass

        doberman.display();
        // call method of superclass with the object of subclass
        doberman.eat();
        /*
        is-a relationship
        In Java, inheritance is an is-a relationship. That is, we use inheritance only if there exists an is-a relationship between two classes. For example,

        Car is a Vehicle
        Orange is a Fruit
        Surgeon is a Doctor
        Dog is an Animal
        */
        
    }
}