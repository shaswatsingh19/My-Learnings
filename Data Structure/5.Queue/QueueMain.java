import java.util.*;
class ImplementQueue{

    private List<Integer> queue;
    private int start;
    public ImplementQueue(){
        queue = new ArrayList<Integer>();
        start = 0;
    }

    public boolean enQueue(int x){
        queue.add(x);
        return true;
    }

    public boolean deQueue(){
        if(isEmpty() == true){
            return false;
        }
        start++;
        return true;
    }

    public boolean isEmpty(){
        return start >= queue.size(); 
        
    }

    public int front(){
        return queue.get(start);
    }

}


public class QueueMain{
    public static void main(String [] args){
        ImplementQueue q = new ImplementQueue();
        Scanner in = new Scanner(System.in);
        if(q.isEmpty() == false){
            
            System.out.println(q.front());
        }
        else{
                        System.out.println("Queue is empty");

        }

        q.enQueue(12);
        q.enQueue(2);
        if(q.isEmpty() == false){
            
            System.out.println("Front element is "+q.front());
        }
        q.deQueue();
        q.deQueue();
        

        q.enQueue(88);
        q.enQueue(5);

        if(q.isEmpty() == false){
            
            System.out.println("Front element is "+q.front());
        }
    }
}