class BinarySearchUsingRecursion{
    public static void main(String[] args) {
        int [] arr = {1,2,3,4,5,6};
        int find = 1;
        BinarySearchUsingRecursion obj = new BinarySearchUsingRecursion();

        int res = obj.BinarySearch(arr,find,0,arr.length-1);

        if(res==-1){
            System.out.println("NOT VALID or NOT PRESENT");
        }
        else{
            System.out.println("THE ELEMENT IS PRESENT AT "+res);
        }
        

    }

    int BinarySearch(int arr[],int x,int start,int end){
        
        if(arr.length==0 || start>end){
            return -1;
        }
        // We use this formula as it doesn't give overflow as mid = (start+end)/2; should gives overflow
        int mid = start + (end-start)/2;

        if( x == arr[mid]){
            return mid;
        }

        else if( x < arr[mid]){
            return BinarySearch(arr, x, start, mid-1);
        }
        else{
            return BinarySearch(arr, x, mid+1, end);
        }
        

    }
}