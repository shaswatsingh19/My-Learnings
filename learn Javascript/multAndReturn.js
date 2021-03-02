arr = [2,3,4,6,8]

const newArr = arr.filter( (el) =>{ 
    return el>4;
});

console.log(newArr) // [6,8]


const newArr1 = arr.map( (el,ind) => {
    return el+" at index "+ind
})


console.log(newArr1) // [ false, false, false, true, true ]

const newArrFor = arr.forEach( (el)=>{
    return el;
});

console.log(newArrFor) ; // return undefined but map returns array

const multByTwo = arr.map( (el)=>{

    return el*2; // [ 4, 6, 8, 12, 16 ] now below line is el>10
}).filter( (el)=>{
    return el>10; [12,16]
})

console.log(multByTwo)

console.log(arr)