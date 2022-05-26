let arr = [1,2,3,4,5]

function double(el){
    return el*2
}
arr.forEach(function (el){
    console.log(el* 2)
})


const doubledArray = arr.map(double)

console.log(doubledArray)


const thripledArray = arr.map( el => el*3)

console.log(thripledArray)

// it terms of performance map is faster than forEach
const myAwesomeArray = [1, 2, 3, 4, 5]

const startForEach = performance.now()
myAwesomeArray.forEach(x => (x + x) * 1000000000)
const endForEach = performance.now()
console.log(`Speed [forEach]: ${100*(endForEach - startForEach)} miliseconds`)

const startMap = performance.now()
myAwesomeArray.map(x => (x + x) * 1000000000)
const endMap = performance.now()
console.log(`Speed [map]: ${100*(endMap - startMap)} miliseconds`)


const scores = [
    { name: 'Asabeneh', score: 95 },
     { name: 'Lidiya', score: 98 },
    { name: 'Mathias', score: 80 },
    { name: 'Elias', score: 50 },
    { name: 'Martha', score: 85 },
    { name: 'John', score: 100 },
  ]
  
  const scoresGreaterEighty = scores.filter((score) => score.score > 80)
  console.log(scoresGreaterEighty)