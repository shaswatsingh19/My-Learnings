import java.util.Arrays;

public class SortingInsertionSort {
    static void insertion(int [] arr){
        int n = arr.length;
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i -1;
            while(j>=0 && arr[j]>key){
                arr[j+1] = arr[j];
                j--;
            }
            arr[j+1] = key;
        }
    }
    public static void main(String[] args) {
        int arr[]  = {7,2,1,6,8,5,3,4};
        insertion(arr);
        System.out.println(            Arrays.toString(arr));
    }
}
