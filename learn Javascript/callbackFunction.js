// what is Callback Function in JSON

// function are first class citizen i.e we can pass fucntion as a argument inside another function 
// The fucntion that is passed as an argument is callback fucntion 

// Js is a synchronous and single thread language 

setTimeout( function f() {
    console.log('Ran after 5sec')
} , 5000) 

console.log('This line run as settimeout will wait for 5sec, and with the help of setTimeout we here make js async')

// blocking the main thread
// with the help of async we don't block the call stack (main thread) which is good and 
// sometimes we block the main thread and the below code doesn't work 
// always use async which takes time 


// Garbage collections & removeEventListener

//EVENTLISTENER are heavy
// so when not in use remove listener