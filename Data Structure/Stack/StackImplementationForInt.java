public class StackImplementationForInt {
    private int arr[];
    private int top;
    private int capacity;

    // Creating a Stack 
    StackImplementationForInt(int size){
        arr = new int [size];
        capacity = size;
        top = -1;
    }

    // Inserting onto Stack
    public void push(int data){
        if(isFull()) {
            System.out.println("OVERFLOW\nProgram terminated");
            System.exit(0);
        }
        System.out.println("Inserting..."+data);
        arr[++top] = data;
    }

    // Removing from the Stack
    public int pop(){
        if (isEmpty()){
            System.out.println("STACK is Empty");
            System.exit(0);
        }
        return arr[top--];
    }
    // see top element
    public int peek(){
        return arr[top];

    }
    // Utility function to return Size of Stack
    public int size(){
        return top+1;
    }

    // Check if Stack is Full
    boolean isFull(){

        return top == capacity - 1;
    }

    // Check if Stack is Empty
    boolean isEmpty(){
        return top == -1;
    }

    // Printing the Stack 

    public void printStack(){
        for(int i = 0;i<=top;i++){
            System.out.println(arr[i]);
        }
    }
    
    
    
    public static void main(String[] args) {
        


        StackImplementationForInt stack = new StackImplementationForInt(12);

        stack.push(3);
        stack.push(13);
        System.out.println(stack.pop());
        
        

    }
}
