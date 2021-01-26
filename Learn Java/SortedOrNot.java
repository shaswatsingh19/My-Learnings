public class SortedOrNot {
    public static void main(String[] args) {
        int [] num = new int [4];
        num[0] = 1;
        num[1] = 11;
        num[2] = 1;
        num[3] = 1123;
        boolean flag = true;
        for (int i = 0 ; i<num.length-1;i++){
            if (num[i]>num[i+1]){
                flag = false;
                break;
            }
        }
        if (flag==true){
            System.out.println("ARRAY IS SORTED");
        }
        else
        {
            System.out.println("ARRAY IS NOT SORTED");
        }
    }
}
