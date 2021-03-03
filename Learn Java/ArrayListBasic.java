import java.util.ArrayList;
import java.util.Collection;
import java.util.*;
import java.util.Iterator;
// ArrayList is a class that implements List sub interface which extendss Collection Interface
// declaration ==> public class ArrayList<E> extends AbstractList<E> implements List<E>, RandomAccess, Cloneable, Serializable  
public class ArrayListBasic {
    public static void main(String[] args) {

        ArrayList<Integer> l1 = new ArrayList<>();

        // adding 
        l1.add(55);
        l1.add(51);
        l1.add(99);

        System.out.println(l1); // [55,51,99]

        l1.add(1,88); // adding at 1 index

        
        System.out.println(l1); // [55,88,51,99]

        // get a element by index

        int getElementByIndex = l1.get(2); 

        System.out.println(getElementByIndex); // 51

        // setting a element means changing an element

        l1.set(1, 5);

        System.out.println(l1); // [55,5,51,99]

        // remove an element

        l1.remove(2); // [55,5,99]

        System.out.println(l1);

        


        // iterate through ArrayList

        for(int i:l1){
            System.out.println(i);
        }


        // ArrayList to Array

        Integer[] arr = new Integer[l1.size()];

        l1.toArray(arr);

        for(int i:arr){
            System.out.print(i+" ");
        }
        System.out.println();

        // CHeck whether it is empty or not 

        System.out.println(l1.isEmpty());


        // ArrayList list=new ArrayList();

        // list.add(22);
        // list.add("dsad");

        // System.out.println(list);
        // non generic way to make arrayList 



        // iterate using iterator

        Iterator itr =l1.iterator();

        while(itr.hasNext()){
            System.out.print(itr.next());
        }

        // sorting arraylist

        Collections.sort(l1);  



















        // Remove all the elemtn from list

        l1.clear();

        System.out.println(l1); // []
    }
}
