var a = 1;
var b = 2;

if( a<b){

    console.log("1 is less than 2")
}
else if (a>b){
    console.log(a+" > than "+b)
}
else{
    console.log(a+" == "+b)
}
var i = 0
while (i<10){
    console.log(i);
    i++;
}


var students={
    "name":"shaswat",
    "class":12,
    "roll":92
}
for (const key in students) {
    if (Object.hasOwnProperty.call(students, key)) {
        const element = students[key];
        console.log(element)
    }
}


a = 10;
b = 20;
// ternerary operator

console.log(a>b?"a is greater":"b is greater");

// for 
// for (let index = 0; index < array.length; index++) {
//     const element = array[index];
    
// }

for(let i=1;i<11;i++){
    console.log(5+" x "+i+" = "+ (5*i));
}

// number = parseInt(prompt('Enter a number: '));
// console.log(number)