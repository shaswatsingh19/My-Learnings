{/* <script> */}
 
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
        
        for (i = 0 ;i<arr_size;i++){
            if (arr[i]>largest){
                second = largest ;
                largest = arr[i]
            }

            else if (arr[i]!=largest && arr[i]>second ){
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
    

    // Driver program to test above function 
 
    let arr= [ 12, 35, 1, 10, 34, 1 ];
    let n = arr.length;
    print2largest(arr, n);
 
 
// </script>