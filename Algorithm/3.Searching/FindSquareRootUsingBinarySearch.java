class SquareRoot
{
    long floorSqrt(long x)
	{
        long ans=0;
        long start=0;
        long end = x;
        while(start<=end){
            long mid = start + (end-start)/2;
            
            if(mid*mid==x){
                return mid;
            }
            else if(mid*mid < x){
                ans = mid;
                start = mid + 1;
            }
            else{
                end = mid - 1;
            }
            
        }
        return ans;
	 }
}
public class FindSquareRootUsingBinarySearch {
    public static void main(String[] args) {
        long x = 15;

        SquareRoot obj = new SquareRoot();

        long ans = obj.floorSqrt(x);

        System.out.println(ans);

    }
    
}
