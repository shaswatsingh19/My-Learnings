// Find the two non repeating element in an array where every other element appears twice
// using XOR 
/*
1:do xor of all element and we find those two unique element
2:do b = a & negation(a-1) of the result and find the element which is righmost set bit
3:make two variable and insert the xor with b to all element and insert in group 1 else group 2
 */
public class FindElement2 {

    public static void findElement2( int []arr,int n){
        int res = 0;
        for (int i =0;i<n;i++){
            res = res ^ arr[i];
        }
        res = res & -res;

        int sum1=0;
        int sum2=0;
        for (int i=0;i<n;i++){
            if ((res&arr[i])==1) sum1=sum1^arr[i];
            else sum2 = sum2^arr[i];
        }
        System.out.println("THE two non repeating number are "+sum1 +" and "+sum2);

    }
    public static void main(String[] args) {
        int [] arr = new int[]{1,2,3,4,7,3,2,1};
        int n  = arr.length;
        findElement2(arr,n);
    }
}
