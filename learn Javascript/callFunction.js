
let name = {
    firstName :"Shaswat",
    lastName : "Singh",
    printFunction(){
        console.log(this.firstName+" "+this.lastName)
    }
}

name.printFunction() // Shaswat Singh

let printFunction = function(homeTown){
    console.log("my Name is "+this.firstName +" "+this.lastName +" from "+ homeTown)
}

let name2 = {
    
    firstName :"Shivam",
    lastName : "kumar"
}

printFunction.call(name2,"Agra") // my name is shivam kumar
// with help of call function we can reduce the complexity and increase the functionality of the application
name.printFunction.call(name2) // shivam kumar

// if we got more argument then we can use apply in place of call just it take input in array format


let printName = printFunction.bind(name2,'Sagar')
console.log(printName) // bind return a function that can be called later the line
printName()