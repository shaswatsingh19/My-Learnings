abstract class NewClass{
    public void show(){
        System.out.println("RUNNING THE METHOD OF ABSTRACT CLASS");
    }
}

class AbstractClassMethod extends NewClass{
    public static void main(String[] args) {
        AbstractClassMethod obj  = new AbstractClassMethod();

        obj.show();
        
    }
}