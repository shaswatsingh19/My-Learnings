// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// class Solution {
//     public int maxProfit(int[] prices) {
//         int b = 10000;
//         int s = 0;
//         int p  = 0;
//         if(prices.length <2 ) {
//             return 0;
//         }
//         for (int i= 0;i<prices.length-1;i++){
//             if (prices[i] < b) {
//                 b = prices[i];
//             }
//             else if (prices[i] - b > s && prices[i] >= prices[i+1]){
//                 s = prices[i];
//                 p += prices[i] - b;
//                 b = 10000;
//                 s=0;
//             }
//             // else  if (prices[i] < b){
//             //     b = prices[i];
//             //     s =0;
//             // }
//         }
//         if (prices[prices.length-1] > prices[prices.length-2]){
//             s = prices[prices.length-1];
//             p += s - b;
//         }
        
//         return p;
    
//     }
// }


class Solution {
    public int maxProfit(int[] prices) {
        int maxprofit = 0;
        for (int i = 1; i < prices.length; i++) {
            if (prices[i] > prices[i - 1])
                maxprofit += prices[i] - prices[i - 1];
        }
        return maxprofit;
    }
}