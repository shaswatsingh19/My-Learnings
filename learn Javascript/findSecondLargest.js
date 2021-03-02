
// Javascript program to find second largest
// element in an array
  
    // Function to print the second largest elements 
    function print2largest(arr, arr_size) {
        let i;
        let largest = second = -2454635434;
  
        // There should be atleast two elements 
        if (arr_size < 2) {
            document.write(" Invalid Input ");
            return;
        }
  
        // finding the largest element 
        for (i = 0;i<arr_size;i++){
        	if (arr[i]>largest){
            	largest = arr[i];
            }
        }
  
        // Now find the second largest element
        for (i = 0 ;i<arr_size;i++){
        	if (arr[i]>second && arr[i]<largest){
            	second = arr[i];
        	}
        }
 
    	if (second == -2454635434){
        	
        document.write("There is no second largest element<br>");
        }
    	else{
	        document.write("The second largest element is " + second);
                return;
            }
        }
    

print2largest([1,2,3,4,9,2,6],7);


// Complexity Analysis:

// Time Complexity: O(n). 
// Two traversals of the array is needed.
// Auxiliary space: O(1). 
// As no extra space is required.