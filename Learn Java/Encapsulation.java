class Person{
    private int age;

    public void getAge() {
         System.out.println(this.age);;
    }

    public void setAge(int age) {
        this.age = age;
    }

}

public class Encapsulation {
    public static void main(String[] args) {
        Person obj = new Person();

        obj.getAge(); // 
        obj.setAge(25);
        obj.getAge();
    }
    
}

/*
Encapsulation refers to the bundling of fields and methods inside a single class.

It prevents outer classes from accessing and changing fields and methods of a class. This also helps to achieve data hiding.
This is only encapsulation. We are just keeping similar codes together.

Note: People often consider encapsulation as data hiding, but that's not entirely true.

Encapsulation refers to the bundling of related fields and methods together. This can be used to achieve data hiding. Encapsulation in itself is not data hiding.

The getter and setter methods provide read-only or write-only access to our class fields. For example,
getName()  // provides read-only access
setName() // provides write-only access
It helps to decouple components of a system. For example, we can encapsulate code into multiple bundles.

These decoupled components (bundle) can be developed, tested, and debugged independently and concurrently. And, any changes in a particular component do not have any effect on other components.
 */