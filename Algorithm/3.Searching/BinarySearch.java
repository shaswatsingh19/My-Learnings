public class BinarySearch {

    int binarySearch(int []arr, int n){
        // n = 12 min = 6 max =6 mid = 5 {12,42,53,64,75,777,997,1000};
        int min = 0;
        int max = arr.length ;
        while (min<max){
            int mid = (min + max) /2;
            if (arr[mid]<n){
                min = mid;
            }
            else if (arr[mid]>n){
                max= mid;
            }
            else{ 
                return mid;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        BinarySearch obj  = new BinarySearch();
        int []arr = {12,42,53,64,75,777,997};
        int n = 997;
        int ans = obj.binarySearch(arr, n);
        if (ans==-1) System.out.println("NOt found");
        else System.out.println("found at "+ (ans+1) +" position");
    }
    
}
