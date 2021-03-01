class Polygon2 {

    // method to render a shape
    public void render() {
      System.out.println("Rendering Polygon...");
    }
  }
  
  class Square2 extends Polygon2 {
  
    // renders Square
    public void render() {
      System.out.println("Rendering Square...");
    }
  }
  
  class Circle2 extends Polygon2 {
  
    // renders circle
    public void render() {
      System.out.println("Rendering Circle...");
    }
  }
  
  class Polymorphism {
    public static void main(String[] args) {
      
      // create an object of Square
      Square2 s1 = new Square2();
      s1.render();
  
      // create an object of Circle
      Circle2 c1 = new Circle2();
      c1.render();
    }
  }


  /*
  We can achieve polymorphism in Java using the following ways:

    1.Method Overriding
    2.Method Overloading
    3.Operator Overloading

   */