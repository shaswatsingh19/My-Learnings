class Factorial{

    int factUsingLoop(int n){
        int ans=1;
        for (int i = 1;i<=n;i++){
            ans = ans * i;
        }
        return ans;
    
    }

    long factUsingRecursion(long n){
        if (n<2) return 1;
        else{
            return  n*factUsingRecursion(n-1);
        }
    }
    public static void main(String[] args) {


        Factorial obj = new Factorial();

        int n = 20;
        System.out.println(obj.factUsingLoop(n)) ;
        System.out.println(obj.factUsingRecursion(n));
    }
}