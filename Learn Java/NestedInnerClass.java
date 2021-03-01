class CPU {
    double price;
    // nested class
    class Processor{

        // members of nested class
        double cores;
        String manufacturer;

        double getCache(){
            return 4.3;
        }
    }

    // nested protected class
    protected class RAM{

        // members of protected nested class
        double memory;
        String manufacturer;

        double getClockSpeed(){
            return 5.5;
        }
    }
}

public class NestedInnerClass {
    public static void main(String[] args) {

        CPU cpu = new CPU();

        CPU.Processor processor = cpu.new Processor();

       System.out.println( processor.getCache());

        CPU.RAM ram = cpu.new RAM();

        System.out.println(ram.getClockSpeed());
     }
}
