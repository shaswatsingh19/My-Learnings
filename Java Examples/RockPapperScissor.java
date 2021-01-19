import java.util.Scanner;
public class RockPapperScissor {
    public static void main(String[] args) {
        Scanner in= new Scanner(System.in);
        
        System.out.println("Enter Player 1 Name");
        String p1 = in.next();
        System.out.println("Greeting to "+p1);
        
        System.out.println("Enter Player 2 Name");
        String p2 = in.next();
        System.out.println("Greeting to "+p2);

        
        System.out.println("Choose your move "+p1+" from ROCK , PAPER and SCISSOR");
        String m1 = in.next();
        System.out.println("Choose your move "+p2+" from ROCK , PAPER and SCISSOR");
        String m2 = in.next();
        String win = "";
        if (m1=="ROCK"){
            if (m2=="PAPER") win = "p2";
            else win = "p1";
            System.out.println("@231232");
        }
        else if (m1=="PAPER"){
            if (m2=="ROCK") win = "p1";
            else win = "p2";
        }
        else if (m1=="SCISSOR") {
            if (m2== "ROCK") win = "p2";
            else win = "p1";
        }
        else{
            win = "DRAW";
        }
        

        // if (win == "p1"){
        //     System.out.println(p1+" Wins the GAme");
        // }
        // else{
        //     System.out.println(p2+" Wins the GAme");
        // }
        System.out.println(p1 + m1 + p2 + m2  + win);
        
    in.close();
        
    }
}
