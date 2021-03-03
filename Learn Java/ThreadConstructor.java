class MyTh extends Thread{

    public void Thread(String name){
        System.out.println(name);
    }

    public void run(){

    }
}

class MyTh2 extends Thread{

    public void Thread(String name){
        System.out.println(name);
    }

    public void run(){

    }
}
class ThreadConstructor{
    public static void main(String[] args) {

        MyTh t1 = new MyTh();
        t1.Thread("shaswat");
        t1.start(); 

        System.out.println(t1.getId());
        
        System.out.println(t1.getName());

        MyTh2 t2= new MyTh2();
        t2.Thread("singh");

        System.out.println(t2.getId());
        
        System.out.println(t2.getName());
        
        t1.setPriority(1);
        t2.setPriority(Thread.MAX_PRIORITY);
    }
}