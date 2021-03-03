

class MyThread1 extends Thread{
    @Override
    public void run(){
        while(true){
            
        System.out.println("THE THREAD IS RUNNING...");
        }
    }
}




class MyThread2 extends Thread{
    @Override
    public void run(){
        while(true){
            
        System.out.println("abc");
        }
    }
}

public class ThreadByExtendingClass {
    public static void main(String[] args) {
        MyThread1 t1 = new MyThread1();
        MyThread2 t2 = new MyThread2();
        t1.start();
        t2.start();
        
        
    }
}
