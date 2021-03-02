ar = [
    2,3,
    4,5
]

const sum = (ar.reduce( (accumulator,current)=>{
    return  accumulator += current;

},7)); // here 7 is treated as initial value

console.log(sum)



const multi = (ar.reduce( (accumulator ,current)=>{
    return  accumulator*= current;

}));

console.log(multi)


ar  = [[2,3],["lion","cub"]]
console.log(ar.reduce( (accum,current) => {
    return accum.concat(current);
}));