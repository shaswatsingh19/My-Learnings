public class ReverseAString {
    public static void main(String[] args) {
        // Method 1
        String st = "atTheRate";

        for(int i=st.length()-1;i>-1;i--){
            System.out.print(st.charAt(i)+"");
        }
        System.out.println();
        // Method 2
        st = "hash map";

        StringBuilder str = new StringBuilder(st);

        System.out.println(str.reverse());
        str.append("ssss");
        System.out.println(str);
        
        // Method 3
        
      }
}
