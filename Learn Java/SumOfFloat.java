public class SumOfFloat {
    public static void main(String[] args) {
        float [] value = new float [] {1f,2f,3f,4f};


        float summ=0f;
        for (int i =0;i<value.length;i++){
            summ += value[i];
        }
        System.out.println(summ);

        float avg=0;
        for(float a : value){
            avg+= a;
        }
        System.out.println(avg/value.length);

    }
}
