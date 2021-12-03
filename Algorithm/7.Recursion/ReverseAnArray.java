class reverseAnArray{

    public static int Rev(int i,int [] arr ,int n){
        if(i<=n/2){
            int temp = arr[i];
            arr[i] = arr[n];
            arr[n] = temp;
            return Rev(i+1,arr,n-1);
        }
        return 0;
    }
    
    public static void main(String[] args){
        System.out.println("Array Before:");
        int [] arr = {3,5,1,22,6,65,0};
        for(int i:arr){
            System.out.print(i+" ");
        }
        int n = arr.length;
        Rev(0,arr,n-1);


        System.out.println();
        System.out.println("Array After:");  
        for(int i:arr){
            System.out.print(i+" ");
        }

    }
}