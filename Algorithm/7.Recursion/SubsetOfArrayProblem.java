import java.util.*;
class SubsetOfArrayProblem{

    public static void subset(int i,int [] arr,ArrayList<Integer> al,int n){
        if(i==n){
            System.out.println(al);
            return;
            
        }
            al.add(arr[i]);
            subset(i+1,arr,al,n);
            al.remove(al.size()-1);
            subset(i+1,arr,al,n);

    }

    
    public static void main(String[] args){
        int [] arr = {1,5,2};
        int n = arr.length;
        ArrayList<Integer> al = new ArrayList<>();
        subset(0,arr,al,n);


    }
}