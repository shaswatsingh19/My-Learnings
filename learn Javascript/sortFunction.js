// works as a string 

ar = ["jan","feb","mar","apr","may"]

console.log(ar.sort()) //[ 'apr', 'feb', 'jan', 'mar', 'may' ]

console.log(ar.reverse()) // [ 'may', 'mar', 'jan', 'feb', 'apr' ]

arr = [32,1,10000000,9,54]

console.log(arr.sort()) // [ 1, 10000000, 32, 54, 9 ]
// it sort by first converting into string and then sorting 

/*
ar.push(element) // insert to last
ar.pop () // remove from last
ar.unshift(element) // insert to start
ar.shift() // remove from start
*/

ar.splice(0,1);

console.log(ar)