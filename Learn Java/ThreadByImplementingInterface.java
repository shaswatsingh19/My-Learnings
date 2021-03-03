class MyThreadRunnable implements Runnable{
    public void run(){
        for (int i=1;i<101;i++){
            System.out.println("5 X "+i+" = "+(5*i));
        }

    }
}

class MyThreadRunnable1 implements Runnable{
    public void run(){
        for (int i=1;i<101;i++){
            System.out.println("17 X "+i+" = "+(17*i));
        }

    }
}

public class ThreadByImplementingInterface {
    public static void main(String[] args) {

        MyThreadRunnable obj = new MyThreadRunnable();
        Thread t1 = new Thread(obj);

        MyThreadRunnable1 obj1 = new MyThreadRunnable1();

        Thread t2= new Thread(obj1);

        t1.start();
        t2.start();
        
    }
}
