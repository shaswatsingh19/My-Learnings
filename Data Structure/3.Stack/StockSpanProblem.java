import java.util.ArrayList;
import java.util.Arrays;


public class StockSpanProblem {
    public static void main(String[] args) {
        ArrayList<Integer> arr = new ArrayList<>();
        arr.add(100);
        arr.add(80);
        arr.add(60);
        arr.add(70);
        arr.add(60);
        arr.add(75);
        arr.add(85);

        int size = arr.size();

        StackImplementationForInt stack = new StackImplementationForInt(size);
        int [] span = new int[size];

        int i = 0;
        int j = 0;

        while(i<size){
            if(stack.isEmpty()){
                span[i] = 1;
                stack.push(arr.get(i));
                i++;
            }
            else if(arr.get(i) < stack.peek()){
                j = arr.indexOf(stack.peek());
                span[i] = i -j ;
                stack.push(arr.get(i));
                i++;
            }

            else if(arr.get(i) >= stack.peek()){
                stack.pop();
            }
        }


        System.out.println(Arrays.toString(span));
    }

}
