class PowerOfN{
    static int pow(int x,int y){
        if(y==0) return 1;

        return x*pow(x,y-1);
    }
    public static void main(String[] args){

        int x = 2;
        int y = -3;

        System.out.println("The value of "+x+" to the power of "+y+" is : "+pow(x,y));
    }
}