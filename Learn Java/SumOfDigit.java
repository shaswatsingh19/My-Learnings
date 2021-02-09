class SumOfDigit{
    public static void main(String[] args) {
        int num = -10;
        int sum = 0;
        if (num<0){
            num = num * -1;
        }
        while(num>0){

            int rem = num%10;
            sum += rem;
            num /= 10;
        }
        System.out.println(sum);

    }

}    