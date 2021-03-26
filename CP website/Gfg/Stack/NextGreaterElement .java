/*
Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

Example 1:

Input: 
N = 4, arr[] = [1 3 2 4]
Output:
3 4 4 -1
Explanation:
In the array, the next larger element 
to 1 is 3 , 3 is 4 , 2 is 4 and for 4 ? 
since it doesn't exist, it is -1.
*/
class Solution{
    public static long[] nextLargerElement(long[] arr, int n) { 
        // Your code here
        int i = n-1;
        int j = 0;
        Stack <Long> stack = new Stack<>();
        long [] near = new long[n];
        
        while(i>-1){
            
            
            if(stack.empty()){
                near[j] = -1;
                stack.push(arr[i]);
                j++;
                i--;
            }
            else if( stack.peek() > arr[i]){
                near[j] = stack.peek();
                stack.push(arr[i]);
                i--;
                j++;
            }
            
            else if (stack.peek() <= arr[i]){
                stack.pop();
            }
            
        }
        int start = 0;
        int end = n-1;
        while(start<end){
            long temp = near[start];
            near[start] = near[end];
            near[end] = temp;
            start++;
            end--;
            
        }
        return near;
        
    } 
}