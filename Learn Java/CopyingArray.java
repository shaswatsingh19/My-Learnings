import java.util.Arrays;

public class CopyingArray {
    public static void main(String[] args) {
        // Method 1 :- using assignment operator

        int [] ar1 = {1,2,3,4};
        int [] ar2 = ar1;

        ar1[0] = -1;
        
        for (int e:ar2){
            System.out.println(e);
        }
        // But the main problem is that if we change value in one array other should also get changed 

        // Method 2 :- copying using loop

        int [] num1 = new int[3];
        int [] num2 = new int[3];
         
        num1[0] = 5;num1[1] = 11;num1[2] = 0;
        
        for(int i=0;i<num1.length;i++){
            num2[i] = num1[i];
        }
        System.out.println(Arrays.toString(num2)); // [5, 11, 0]
        // If we change any element in num1 corresponding element doesn't change as both are 
        // referred to different object 
        num1[0] = 999;
        System.out.println(Arrays.toString(num1)); // [999, 11, 0]
        System.out.println(Arrays.toString(num2)); // [5, 11, 0]
        

        // Method 3 :- using arraycopy() method which copy one to another array
       //  Syntax :- arraycopy(Object src, int srcPos,Object dest, int destPos, int length)

       int [] arr1={1,2,3,4};
       int [] arr2 = new int[4];
       System.out.println(Arrays.toString(arr2)); // [0, 0, 0, 0]
       
       System.arraycopy(arr1, 0, arr2, 0, 4);
       
       System.out.println(Arrays.toString(arr2)); // [1, 2, 3, 4]

       // Method 4 :- Using copyOfRange() from Arrays class
       // Syntax :- Arrays.copyOfRange(original, from, to)

       String [] name= {"goku","chichi","gohan","yoda"};

       String [] newName = Arrays.copyOfRange(name, 0,name.length);

       System.out.println(Arrays.toString(newName));  //{"goku","chichi","gohan","yoda"};

       
    }
}
