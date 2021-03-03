public class InsertElementInArray {

    int count=0;
    public static void main(String[] args) {

        InsertElementInArray o = new InsertElementInArray();

        int [] arr = new int[5];

        for(int i=0;i<arr.length;i++){
            o.insertAtEnd(arr, 5*i);

        }

        int [] arr1 = new int[5];
        
        for(int i=0;i<arr.length;i++){
            o.insertAtStart(arr1, 4+i);

        }




        // printing the array
        for(int i=0;i<arr.length;i++){
            System.out.println(arr[i]);
        }
        System.out.println("----------------------------------------------------");
        for(int i=0;i<arr.length;i++){
            System.out.println(arr1[i]);
        }
        
         

    }


    void insertAtEnd(int arr[],int x){
        arr[count++] = x;
    }

    void insertAtStart(int arr[] , int x){
        // arr[1,2,3,4,5]
        for(int i=arr.length-2;i>=0;i--){
            arr[i+1]=arr[i];
        }
        arr[0] = x;
    }
}
