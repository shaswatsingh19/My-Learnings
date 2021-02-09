import java.util.Scanner;

public class LinearSearch {

    int linearSearch(int [] arr, int target){
        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == target){
                return (i+1);
           }
        }
        return 0;
  
    }
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int [] arr = new int[5];
        LinearSearch obj = new LinearSearch();
        for (int i = 0; i < arr.length; i++) {
            arr[i] = in.nextInt();
        }
        System.out.print("Enter the number to find: ");
        int target = in.nextInt();
        int ans = obj.linearSearch(arr,target);
        
        if (ans==0) System.out.println(target +" is not present in array");
        else{
            System.out.println(target + " is present at " + ans +" position");
        }
        

        in.close();
    }
}
