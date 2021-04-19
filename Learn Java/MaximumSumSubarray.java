class MaximumSumSubarray{
    public static void main(String[] args) {
        int [] arr = {-1,-2,-3};

        int bestMax = 0;
        int currentMax = 0;
        for (int i = 0; i < arr.length; i++) {
            currentMax += arr[i];

            if (currentMax>0 && currentMax>bestMax){
                bestMax = currentMax;
            }
            if(currentMax<0){
                
            currentMax = 0;
            }
        }
        System.out.println(bestMax);
    }
}