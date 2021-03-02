
a = ["hello","world","my","beautiful","people"]
console.log(a)

// gives index of a
for (let ele in a){
    console.log(ele);
}

// give element of a
for (let ele of a){
    console.log(ele)
}


// gives element , index and shows the array we are working in
a.forEach( function(el,index,array){

    console.log(el,index,array);
});


a.forEach((ele,ind,arr) => {
    console.log(ele,ind,arr)

})


arr = [1,2,3,4,5]

const fil = arr.filter( (el,index) => {
    return (el)>2;
}); // return after filtering the true condition


console.log(fil)