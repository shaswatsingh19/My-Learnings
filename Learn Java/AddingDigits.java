// https://codeforces.com/problemset/problem/260/A
import java.util.Scanner;
class AddingDigits{
    public static void main(String [] args){
        Scanner in  = new Scanner(System.in);

        int a = in.nextInt();//260
        int b = in.nextInt();//150
        int n = in.nextInt();//10
        boolean check  = false;
        for(int i=0;i<n;i++){//i=0
                int temp = a;//260
                temp = temp*10;//2600
            for(int j=0;j<10;j++){
                temp = temp + j;
                if(temp%b==0){
                    check = false;
                    break;
                }
                temp = temp - j;
                check = true;
            }
            if(check){
                break;
            }
            else{
            a = temp;
            }
            // a= 520
        }
        
        System.out.println(a);
    }
}