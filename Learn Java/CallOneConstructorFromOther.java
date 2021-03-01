class Main{


    private int sum;
    private int mult;
    Main(){
        this(11,2); // goes to the below constructor
    }

    Main(int arg1,int arg2){
        this.sum = arg1+arg2;
        this.mult = arg1*arg2;
    }


    int displaySum(){
        return sum;
    }

    int displayMult(){
        return mult;
    }
}


class CallOneConstructorFromOther{

    public static void main(String[] args) {
        

        Main obj = new Main();

       
        System.out.println(obj.displaySum());
        System.out.println(obj.displayMult());
    }
}