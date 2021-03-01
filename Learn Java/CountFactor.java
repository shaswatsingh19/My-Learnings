class CountFactor{
    public static void main(String[] args) {
        int num = 16112;
        int cnt = 0;
        // factor 16  => 1,2,4,8,16
        System.out.print("Factor of "+num+" are:");
        for (int i = 1;i*i<=num;i++){
            if (num%i==0){
                cnt+=1;
                System.out.print(i+" ");
                int div = num/i;
                if (div!=i) {
                    
                System.out.print(div+" ");
                    cnt+=1;
            }
        }
    }
    System.out.println();;
    System.out.println("Factor of "+num+" is :"+cnt);
}
}