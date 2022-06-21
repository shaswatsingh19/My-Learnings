// https://www.geeksforgeeks.org/sum-array-elements-using-recursion/
class SumOfArrayUsingRecursion{

    public static int SumOfArray(int [] arr,int n){
        if(n<=0) return 0;
        return arr[n-1] + SumOfArray(arr,n-1);
    } 


    public static void main(String[] args){
        int [] arr = {4,1,2};
        int n = arr.length;
        
        System.out.println("The sum is "+SumOfArray(arr,n));
    }
}