class Cyl{
    private int radius;
    private int height;

    public int getRadius() {
        return this.radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    public int getHeight() {
        return this.height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public Cyl(){
        radius = 20;
        height = 15;
    }

    public Cyl(int r,int h){
        this.radius = r;
        this.height = h;
    }

    

   
}

public class Cylinder {
    public static void main(String[] args) {

        Cyl ob1 = new Cyl();

        System.out.println(ob1.getRadius());
        System.out.println(ob1.getHeight());


        Cyl ob2 = new Cyl(10,50);

        
        System.out.println(ob2.getRadius());
        System.out.println(ob2.getHeight());


        
    }
}
