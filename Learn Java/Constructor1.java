class Emp2{

    private int id;
    private int salary;

    // As you can see the below we made three constructor
    // this is constructor overloading
    public Emp2(){
        id = 0;
        salary = 0;
    }
    public  Emp2(int s){
        salary = s;
    }

    public Emp2(int id,int salary){
        this.id = id;
        this.salary = salary;
    }

    int getSalary(){
        return salary;
    }

    int getId(){
        return id;
    }

}
public class Constructor1 {
    public static void main(String[] args) {
    
        Emp2 obj = new Emp2(1000);

        System.out.println(obj.getSalary());

        Emp2 obj1 =new Emp2();
        System.out.println(obj1.getSalary());

        Emp2 obj2 = new Emp2(1,500000);
        System.out.println(obj2.getSalary());
    }
}
