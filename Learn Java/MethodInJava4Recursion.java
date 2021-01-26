public class MethodInJava4Recursion {
    
    int fact(int n){
        if (n==1) return 1;
        else{
            return  n* fact(n-1);
        }
        
    }
    
    public static void main(String[] args) {
        int n = 7;
        MethodInJava4Recursion obj = new MethodInJava4Recursion();
        System.out.println(obj.fact(n)); 
    }
}
