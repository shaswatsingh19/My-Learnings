public class Loops {
    public static void main(String[] args) {
        // int i = 1;
        // while (i<10){
        //     System.out.println(i*i);
        //     i+=1;
        // }
        // i = 1;
        // do{
        //     System.out.println(i+1);
        //     i+=1;
        // }while (i<20);

        // for (i = 10;i>0;i--){
        //     System.out.println(i*100);
        // }

        // break and continue

        for (int i = 0;i<10;i++){
            if (i==3) break;
            System.out.println(i);

        }
        System.out.println("--------------------------------");
        for (int i = 0;i<10;i++){
            if (i==3) continue;
            System.out.println(i);

        }
    }
}
