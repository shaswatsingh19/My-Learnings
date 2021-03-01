class Emp1{
    private int id;
    private String name;

    int getId(){return id;}
    void setId(int i) {id = i;} 

    String getName(){return name;}
    void setName(String n) {this.name = n;}


    public Emp1(String n){
        name = n;
    }


}

public class Constructor {
    public static void main(String[] args) {
        
        Emp1 obj = new Emp1("sam");
        System.out.println(obj.getName());// if we run this we get null as write now we didn't initalize it 
        // butt with the help of constructor we can initalize as soon as object is created.
        
        // Now that we construct the constructor we get "sam" just while making the object and it take the value of name
    }
}
