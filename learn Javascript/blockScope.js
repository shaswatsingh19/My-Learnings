// program showing block-scoped concept
// global variable
let a = 'Hello';

function greet() {

    // local variable
    let b = 'World';

    console.log(a + ' ' + b);

    if (b == 'World') {

        // block-scoped variable
        let  c = 'hello';// let is a block scoped but if we use var c it is treated as local variable

        console.log(a + ' ' + b + ' ' + c);
    }

    // variable x cannot be accessed here
    console.log(a + ' ' + b + ' ' + c);
}
greet();