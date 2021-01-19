

public class Chapter4Practice {
    public static void main(String[] args) {
        // // question 1
        // int a = 10;
        // if (a==11) System.out.println("I am 11");
        // else System.out.println("I am not 11");

        // // question 2

        // Scanner in = new Scanner(System.in);

        // double m1 = in.nextDouble();
        // double m2 = in.nextDouble();
        // double m3 = in.nextDouble();

        // double total = (m1+m2+m3)/3;

        // if (total>=40.0 && m1>=33 && m2>=33 && m3>=33){
        //     System.out.println("HE/SHE IS PASSED!");
        // }
        // else{
        //     System.out.println("HE/SHE IS Failed!");
        //     System.out.println("HE/SHE IS Failed!");
            
        // }

        // QUestion 3
//         2.5L – 5.0L  	5%
// 5.0L – 10.0L 	20%
// Above 10.0L	30%
        
    //     Scanner inp = new Scanner(System.in);

    //     double sal = inp.nextDouble();

    //     double tax;
    //     if (sal>=2.5 && sal<=5.0){
    //         tax = ((sal*100000)*5)/100;
    //     }
    //     else if (sal>5.0 && sal<=10.0){
            
    //         tax = ((sal*100000)*20)/100;
    //     }
    //     else if (sal>10.0){
            
    //         tax = ((sal*100000)*30)/100;
    //     }
    //     else{
    //         tax = 0.0;
    //     }
    //     System.out.println("Your Tax is "+tax);
        

    //     inp.close();

//     // question 4
//         Scanner in = new Scanner(System.in);
// //         .com – commercial website
// // .org – organization website
// // .in – Indian website
//             String site = in.next();
//             String siteName ;
//             if (site.endsWith(".com")) siteName = "commercial website";
//             else if (site.endsWith(".org")) siteName =  "organization website";
//             else if (site.endsWith(".in")) siteName = "Indian website";
//             else siteName="Not found";

//             System.out.println(siteName);
            int year = 1400;
            String ans="";
            if (year%100==0){
                if (year%400 == 0) ans = "leap";
                else ans = "Not leap";
            }
             System.out.println("The year is "+ans);




     }

}
