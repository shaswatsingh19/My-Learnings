public class SumUsingVarArgs {


    float sum(int ...ar){
        
        float avg= 0;
        for (int i :ar){
            avg += i;
        }
        float ans = avg / ar.length;
        return ans;
    }
    public static void main(String[] args) {
        SumUsingVarArgs obj = new SumUsingVarArgs();
     System.out.println(obj.sum(1,2,3,4,5));   
    }
}
