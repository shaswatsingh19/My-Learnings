class TryCatch{
    public static void main(String[] args) {
        try{
            int dividebyzero = 4/0;
            System.out.println("DIVIDing by 0 try ends...");

            int [] ar = {1,2};
            int a = ar[50];

        }
        catch(ArithmeticException e){
            System.out.println(e.getMessage()); /// by zero


        }
        catch(IndexOutOfBoundsException e1){
            System.out.println(e1.getMessage()); /// by zero


        }
    }
}