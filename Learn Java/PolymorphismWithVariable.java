
// A variable is called polymorphic if it refers to different values under different conditions, upcasting example in java

class ProgrammingLanguage {
    public void display() {
      System.out.println("I am Programming Language.");
    }
  }
  
  class Java extends ProgrammingLanguage {
    @Override
    public void display() {
      System.out.println("I am Object-Oriented Programming Language.");
    }

    public void show(){
      System.out.println("SHOWING");
    }
  }
  
  class PolymorphismWithVariable {
    public static void main(String[] args) {
  
      // declare an object variable
      ProgrammingLanguage pl;
  
      // create object of ProgrammingLanguage
      pl = new ProgrammingLanguage();
      pl.display();//superclass
  
      // create object of Java class
      pl = new Java();  // Upcasting Parent Class objectName = new Child Class(); with this overriding method can be accesed by parent reference and can only access method not variable
      pl.display();// subclass

      // pl.show() we can't access show method as it is not overridden

    }
  
  }

 