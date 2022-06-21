class Factorial{

    public int fact(int n){
        
        if(n<=1) return n;

        return n*fact(n-1);
    }

    public static void main(String[] args){
        int n = 15;
        Factorial obj = new Factorial();
        System.out.println("Factoria of "+n+" is : "+obj.fact(n));
    }
}