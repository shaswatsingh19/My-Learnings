import java.util.Scanner;

class FindElement {
    int findElement(int [] arr,int x, int n){
        
        for (int i=0;i<n;i++){
            if (arr[i]==x){
                return i;
            }
        }

        return -1;
    }
}

public class FindAnElementIndex {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        FindElement obj = new FindElement();


        int [] arr = new int [6];
        int n = arr.length;
        for (int i=0;i<n;i++){
            arr[i] = in.nextInt();

        }
        System.out.println("ENTER THE ELEMENT TO FIND");
        int x = in.nextInt();

        int res = obj.findElement(arr, x,n);

        if (res==-1) System.out.println("ELEMENT IS NOT PRESENT");
        else{
            System.out.println("ELEMENT FOUND AT index "+res);
        }
    }
}
