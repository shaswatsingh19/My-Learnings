import java.util.Scanner;

public class ReverseStringUsingStack {
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        String str = in.nextLine();
        int size = str.length();
        StackImplementationForInt stack = new StackImplementationForInt(size);

        for (int i = 0; i < str.length(); i++) {
            stack.push(str.charAt(i));
            
        }
        String reversed = "";
        for (int i = 0; i < str.length(); i++) {
            
            reversed += (char)stack.pop();
        }

        System.out.println("original string "+str);
        System.out.println("reversed string "+ reversed);

    in.close();

    }
}
