import java.util.Scanner;

class RotateANumber{
    public static void main(String[] args) {
        
        Scanner in = new Scanner(System.in);

        String n = in.next();
        int k = in.nextInt();

        
        int size = n.length();
        // 12340056
        // 05612340
        StackImplementationForCharacter stack = new StackImplementationForCharacter(size);

        String str = n.substring(n.length()-k, n.length());

        for (int i = n.length()-k-1; i > -1; i--) {
            stack.push(n.charAt(i));
        }

        for (int i = 0; i < n.length()-k; i++) {
            str += (char)stack.pop();
        }
        stack.printStack();
        System.out.println(str);


        in.close();
    }
}