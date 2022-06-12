const container = document.getElementById('container')


container.innerHTML = '<h3>Closure is a function bind together with its lexical environment</h3>'
container.innerHTML += '<h3>Scope of closure </h3>'
container.innerHTML += '<li>Within its own Scope</li>'
container.innerHTML += '<li>Access to variable of outer scope   </li>'
container.innerHTML += '<li>Access to global variable</li>'


function outerFunction(){
    let count = 0
    function innerFunction(){ // closure, and remembers its lexical scope and remember count from heap memory as it stores in heap not in stack 
        count++
        return count
    }
    return innerFunction
}

const innerFunc = outerFunction()
console.log(outerFunction())  // prints out outerfunction 
console.log(outerFunction()())  // calls inner function  or assign it to variable and call it 
console.log(innerFunc())    // 1
console.log(innerFunc())    // 2
console.log(innerFunc())    // 3




function addBy2(){
    const a = 2
    function result(b){
        return a+b
    }
    return result
}

const ans = addBy2()
console.log(ans(5))
console.log(ans) 

container.innerHTML += '<li>outer function doesn\'t have access to inner function</li>'
container.innerHTML += '<li>Used to prevent data leakage, with data abstraction</li>'
container.innerHTML += '<li>outer function values doesn\'t persist it\'s reference will be taken from heap</li>'




function x(){
    let a = 7
    // return function y(){ this version of returing is also correct
    //     console.log(a)
    // }

    function y(){
        console.log(a)
    }
    a = 100 // with 100 written before calling of y it will take a = 100 only as a reference persist not value
    return y 
}


const z = x()
z()