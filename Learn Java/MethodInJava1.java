// to create method we just
// dataType method name() {}
// calling an object => Classname objectName = new Classname();

class MethodInJava1{

    int mySum(int a, int b ){
        return a+b;
    }

    int mySubtract(int a,int b){
        return a-b;
    }
    double myDivide(int a , int b){
        
        return (double)a/b;
    }
    int myMulti(int a , int b){
        return a*b;
    }

    double myMulti(double a,double b){
        return a*b;
    }
    public static void main(String[] args) {
        // calling 
        MethodInJava1 obj = new MethodInJava1();
        
        System.out.println(obj.mySum(2,3));
        System.out.println(obj.myMulti(4, 4));
        
        System.out.println(obj.myDivide(14, 4));
        System.out.println(obj.mySubtract(7, 2));

        MethodInJava1 ob1 = new MethodInJava1();
        System.out.println(ob1.myMulti(3, 11));
        System.out.println(ob1.myMulti(11, 2));
    
    
    
    }
}