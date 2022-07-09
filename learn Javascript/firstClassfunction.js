a() // hoisted 

// b() gives erros as b is undefined and can't call undefined

// function statement or function declaration 

// before starting of code it is declared on the variable env
function a(){
    console.log('a is called')
}

console.log(a) // gives whole function
a()

// function expression => called as a variable

var b = function(){
    console.log("b is called")
}

console.log(b) // will gives whole function


// anonymous function

// function(){
//     console.log('ERROR AS BY ECMA SCRIPT WE SHOULD GIVE A FUNCTION NAME while declaring')
//     console.log('USED when we have to declare fucntion as values')
// }

// AS above we have used anonymouse function is b as value

// but as function statement we can't use it as in a

let div = document.querySelector('div')

div.addEventListener('click',function(){
    console.log('d is clicked')
})


// Named function expression 


var bb = function abc(){
    console.log('bb is called with named expression abc')
}

bb() // gives the console.log value
// abc()   abc is not defined error

// bb.call(bb)  gives sames as bb()



// parameter and argument

function e(parameter){
    console.log('this '+parameter+" is a parameter")
}

e('argument')


// first class function aka first class citizens
// function passed through another function as a argument and used as a value  and returned from function


var fun  = (param) => {
    console.log(param)
}


function newFunction(){
    console.log('this is new function')
}

fun(newFunction)

// newFuntion has been passed as a argument in fun and become a parameter param