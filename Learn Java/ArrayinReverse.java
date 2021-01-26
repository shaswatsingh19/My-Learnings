public class ArrayinReverse {
    public static void main(String[] args) {
        String [] name = new String[] {"Ram","Shyam","RADHA"        };
        for (int i = name.length-1;i>=0;i--){
            System.out.println(name[i]);
        }
        for(String identity:name){
            System.out.println(identity);
        }
    }
}
