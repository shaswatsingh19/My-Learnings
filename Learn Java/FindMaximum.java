public class FindMaximum {
    public static void main(String[] args) {
        int [] marks = new int [] {5,1,2,8,10,7,4};

        int max = -1;
        for (int el:marks){
            if (el>max) max=el;
        }   
        System.out.println("THE MAXIMUM OF THAT ARRAY IS "+max);
    }
}
