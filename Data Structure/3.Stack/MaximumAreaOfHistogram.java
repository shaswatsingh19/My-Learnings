import java.util.ArrayList;


public class MaximumAreaOfHistogram {
    public static void main(String[] args) {
        
        NearestSmallerToLeft left = new NearestSmallerToLeft();

        // int [] arr= {6,2,5,4,5,1,6};
        ArrayList<Integer> arr = new ArrayList<>();

        arr.add(6);arr.add(2);arr.add(5);arr.add(4);arr.add(5);arr.add(1);arr.add(6);

        int size = arr.size();
        int [] nslArr = new int[size];

        left.nsl( arr , size, nslArr);


        NearestSmallerToRight right = new NearestSmallerToRight();

        int [] nsrArr = new int[size];
        right.nsr(arr, size, nsrArr);

        int ans = Integer.MIN_VALUE;
        int max = Integer.MIN_VALUE;
        System.out.println();
        System.out.println("Area Array is :=> ");
        for (int x = 0; x < nslArr.length; x++) {
            int i=-1;
            int j=size;
            if( nslArr[x] != -1) i = arr.indexOf(nslArr[x]);
            
            if (nsrArr[x] != -1) j = arr.indexOf(nsrArr[x]);
            
            ans = (j - i -1)*arr.get(x);
            System.out.print(ans+" ");
            if (ans > max){
                max = ans;
            }
        }
        System.out.println();
        System.out.println("THe maximum area is "+max);
    }
}
