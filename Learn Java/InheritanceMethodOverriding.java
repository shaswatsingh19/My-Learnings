class Fruit{
    void display(){
        System.out.println("I AM A SUPER CLAS FRUIT");
    }
}
class Mango extends Fruit{

    void taste(){
        System.out.println("I TASTE SWEET");
    }
    @Override
    void display(){
        System.out.println("I AM KING OF FRUITS");
    }
}

class Papaya extends Fruit{
    void taste(){
        System.out.println("I TASTE SWEET AND SOUR");
    }
    void display(){
        
    super.display();// using super keyword it first goes to display() of superclass and runs it 
    // then came to child class and runs below lines
        System.out.println("I CONTAIN LOTS OF SEED INSIDE");
    }
}
class InheritanceMethodOverriding{
    public static void main(String[] args) {

        Mango obj = new Mango();
        obj.display();
        obj.taste();

        Papaya obj1 = new Papaya();
        obj1.display();
        obj1.taste();
    }

}