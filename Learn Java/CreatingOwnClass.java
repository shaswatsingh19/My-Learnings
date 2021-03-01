class Employee{
    int id;
    String name;

    public void getDetail(){
        System.out.println("The name of Employee is "+name +" and id is "+id );
    }
    

}

public class CreatingOwnClass {
    public static void main(String[] args) {
        Employee obj = new Employee();

        obj.id = 10;
        obj.name = "John";
        obj.getDetail();

        obj.id = 12;
        obj.name = "doe";
        obj.getDetail();
        
    }
}
