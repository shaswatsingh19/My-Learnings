import java.util.Scanner;

public class StackUsingArray {
    int top=-1;

    void push(int data , int []stk){
        if(isFull(stk)){
            System.out.println("ARRAY IS FULL");
            System.exit(0);
        }
        top++;
        stk[top] = data;
        
    }

    boolean isFull(int []stk){
        if(top == stk.length-1){
            return true;
        }
        return false;
    }

    int pop(int stk[]){
        if(isEmpty()) System.out.println("NOTHING TO POP");
        int temp = top;
        top--;
        return stk[temp];
    }

    boolean isEmpty(){
        if(top == -1) return true;
        return false;
    }

    int peek(int [] stk){
        return stk[top];
    }

    void printArray(int stk[]){
        int i=0;
        while(stk[i]!=0){
            System.out.println(stk[i]);
            i++;
        }
    }

    
    public static void main(String[] args) {

        int [] stk = new int[10];

        StackUsingArray obj = new StackUsingArray();
        Scanner in = new Scanner(System.in);
        
        System.out.println("WELCOME WHAT WOULD YOU LIKE TO DO");
        while(true){

            System.out.println("SELECT ANY OPTION \n 1.PUSH \n 2.POP \n 3.IS STACK FULL \n 4.IS STACK EMPTY \n 5.SEE TOP ELEMENT OF STACK \n 6.SHOW STACK \n 7.EXIT");

            
            int option = in.nextInt();

            if(option==1){
                System.out.println(" => YOU PRESSED FOR PUSH");
                System.out.println("ENTER THE DATA TO PUHS");
                int data = in.nextInt();
                obj.push(data, stk);
            }
            else if(option == 2){
                System.out.println(" => YOU PRESSED FOR POP");
                obj.pop(stk);
            }
            
            else if(option == 3){
                System.out.println(" => CHECKING IF STACK IS FULL...");
                if(obj.isFull(stk)) System.out.println("STACK IS FULL");
                else System.out.println("STACK IS NOT FULL");
            }

            else if(option == 4){
                System.out.println(" => CHECKING IF STACK IS EMPTY");
                if (obj.isEmpty()) System.out.println("STACK IS EMPTY ");
                else System.out.println("STACK IS NOT EMPTY");
            }

            else if(option == 5){
                System.out.println(" => CHECKING TOP ELEMENT OF STACK");
                System.out.println("TOP ELEMENT OF STACK IS "+obj.peek(stk));
            }
            else if (option == 6){
                System.out.println(" => SHOWING THE FULL STACK");
                obj.printArray(stk);
            }
            else{
                System.out.println(" => EXITING THE PROGRAM...");
                break;
            }




            
        }

        in.close();



        
    }
}
