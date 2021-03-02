// Hoisting in JavaScript is a behavior in which a function or a variable can be used before declaration.

greet();

function greet(){
    console.log("hello");}


var a;
console.log(a);
a = 5;

// only var support hoisting

/*
it gives error cannot access 'gr' before initialization
gr();
let gr = function() {
    console.log("sadsdsa")
}

*/