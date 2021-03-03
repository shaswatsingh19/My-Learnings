import java.util.ArrayList;

class Student {
    int roll,age;
    String name;
    Student(String name,int roll,int age){
        this.age = age;
        this.roll = roll;
        this.name =name;
    }

}

class UserDefinedClassInArrayList{
    public static void main(String[] args) {
        Student s1 = new Student("Pan Parag",420,22);
        Student s2 = new Student("Vimal",20,2);
        

        ArrayList<Student> info = new ArrayList<Student>();

        info.add(s1);
        info.add(s2);

        for (Student s : info){
            System.out.println(s.age+" "+s.name+" "+s.roll);
        }

    }
}