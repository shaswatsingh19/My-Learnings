public class SortingQuickSort {

    
     static int partition(int [] arr,int l,int h){
        int pivot = arr[l];

        int i=l;
        int j=h;
        if (i<j){
            while(arr[i]<=pivot && i<j)i++;
            while(arr[j]>pivot && i<j)j--;
            if(i<j){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] =temp;
            }
        }
        int temp = arr[l];
        arr[l] = arr[j];
        arr[j] = temp;
        return j;
    }
    static void quickSort(int []arr,int l,int h){
        if (l<h){
            int j = partition(arr,l,h);
            quickSort(arr, l, j);
            quickSort(arr, j, h);
        }

    }

    static void printArray(int[] arr, int size)
{
    for(int i = 0; i < size; i++)
        System.out.print(arr[i] + " ");
         
    System.out.println();
}

   
    public static void main(String[] args) {
        int [] arr =  {7,2,1,6,8,5,3,4};


        int l = 0;
        int h = arr.length;
        quickSort(arr,l,h-1);
        printArray(arr, h);


    }
}
