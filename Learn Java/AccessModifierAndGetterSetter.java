class Emp{
    private int id;
    private String name;

    int getId(){
        return id;
    }
    void setId(int i){
        id = i;
    }

    String getName(){
        return name;
    }

    void setName(String n){
        name = n;
    }

}


public class AccessModifierAndGetterSetter {
    public static void main(String[] args) {
        Emp obj = new Emp();

        // obj.id = 1;
        // obj.name ="hello"; throws an error
        
        // WE can access variable now as they are private access modifier  this implement encapsulation here
        // we can use public method to access
        System.out.println(obj.getId()); 
        obj.setId(1);
        System.out.println(obj.getId());

        System.out.println(obj.getName());
        obj.setName("Shaktimaan");
        System.out.println(obj.getName());



    }
}
