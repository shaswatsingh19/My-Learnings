import java.util.Scanner;

import java.util.List;

class Remove {
    void removeElement(int [] arr,int x, int n){

        for (int i=0;i<n;i++){
            if(arr[i]==x){
                for (int j = i;j<n-1;j++){
                    arr[j] = arr[j+1];
                }
            }
        }
       
    }
}

public class RemoveAnElement {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        Remove obj = new Remove();


        int [] arr = new int [6];
        int n = arr.length;
        for (int i=0;i<n;i++){
            arr[i] = in.nextInt();

        }
        System.out.println("ENTER THE ELEMENT TO Remove");
        int x = in.nextInt();

        obj.removeElement(arr, x,n);

        for(int i = 0;i<n-1;i++){
            System.out.print(arr[i]+" ");
        }

        
    }
}
