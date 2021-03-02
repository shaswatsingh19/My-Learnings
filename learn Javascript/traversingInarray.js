ar = ["india","pakistan","nepal","usa","russia","uk","usa"]

for (let el of ar){
    console.log(el)
}

ar.forEach((element,index) => {
    console.log(index,element)
});
console.log(typeof(ar)) // object

console.log(ar.toString());

// return 7
console.log(ar.indexOf("usa",5)); // return Index of first occurance and use a number from where to start 


console.log(ar.includes("poland")); // false


arr = [1,2,3,4,5,6]
const findel = (arr.find( (current) => {

    return current>4;
}));

console.log(findel)

