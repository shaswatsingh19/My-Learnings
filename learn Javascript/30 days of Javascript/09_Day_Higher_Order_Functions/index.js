/*
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
*/


console.log('LEVEL 1')


// Explain the difference between forEach, map, filter, and reduce.
console.log("All are higher order function that take a callback function as a argument ")
console.log('ForEach is a function that that array and perform operation and it return undefined')
console.log('Map is similar to forEach but it return a modified array after the logic is been implemented and alos faster than forEach')
console.log('Filter as the name suggest it filter out the array and return a new array based on the logic')
console.log('Reduce help use to accumulate element and perform operation on the array, it return a single value')

// Define a callback function before you use it in forEach, map, filter or reduce.
console.log('Callback function is a regular function that has been used as a argument in some high order function like , map ,sort , filter , some , every , findIndex')

const countries = ['Finland', 'Sweden', 'Egypt','Denmark', 'Norway', 'IceLand']
const names = ['Asabeneh', 'Mathias', 'Elias', 'Brook']
const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
const products = [
    { product: 'banana', price: 3 },
    { product: 'mango', price: 6 },
    { product: 'potato', price: ' ' },
    { product: 'avocado', price: 8 },
    { product: 'coffee', price: 10 },
    { product: 'tea', price: '' },
]


const logging = element => console.log(element) // logging is a callback function
const upperCase = element => element.toUpperCase() // function to make element to upperCase, is a callback function 

// Use forEach to console.log each country in the countries array.
countries.forEach(logging)
// countries.forEach(function(country) {
//     console.log(country)
// })
    
// Use forEach to console.log each name in the names array.
names.forEach(logging)

// Use forEach to console.log each number in the numbers array.
numbers.forEach(logging)


// Use map to create a new array by changing each country to uppercase in the countries array.
const countryUpper = countries.map(upperCase)
console.log(countryUpper)

// Use map to create an array of countries length from countries array.
const countryLength = countries.map(country => country.length)
console.log(countryLength)

// Use map to create a new array by changing each number to square in the numbers array
const square = numbers.map(el =>el*el)
console.log(square)

// Use map to change to each name to uppercase in the names array
const namesUpper = names.map(upperCase)
console.log(namesUpper)

// Use map to map the products array to its corresponding prices.

const prices = products.map(product => `${product.product} : ${product.price}`)
console.log(prices)

// Use filter to filter out countries containing land.
const landInCountry = countries.filter(country => country.toLowerCase().includes('land'))
console.log(landInCountry)

// Use filter to filter out countries having six character.

const CountryWith6Length = countries.filter(country => country.length === 6)
console.log(CountryWith6Length)

// Use filter to filter out countries containing six letters and more in the country array.

const CountryWith6OrMoreLength = countries.filter(country => country.length >= 6)
console.log(CountryWith6OrMoreLength)

// Use filter to filter out country start with 'E';
const CountryStartWithE = countries.filter(country => country.startsWith('E'))
console.log(CountryStartWithE)

// Use filter to filter out only prices with values.
const productWithPrice = products.filter(product => product.price > 0)
console.log(productWithPrice)

// Declare a function called getStringLists which takes an array as a parameter and then returns an array only with string items.

let array = ['hello',1,2,3,'world']
const getStringLists = (arr) => {
    return arr.filter(el => typeof el === "string")
}

const onlyString = getStringLists(array)
console.log(onlyString)

// Use reduce to sum all the numbers in the numbers array.
const sum = numbers.reduce((acc,curr) => acc += curr )
console.log(sum)

// Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and IceLand are north European countries
const allCountries = countries.reduce((acc,curr) => acc = acc+curr+' ', ' ')

console.log(allCountries)

// Explain the difference between some and every
console.log('Some check for true if atleast one condition is True')
console.log('Every check for true if all condition are True')

// Use some to check if some names' length greater than seven in names array
const ifGreaterThan7 = names.some(name => name.length>7)
console.log(ifGreaterThan7)

// Use every to check if all the countries contain the word land
const ifAllContainsLand = countries.every(country => country.toLowerCase().includes('land'))
console.log(ifAllContainsLand)

// Explain the difference between find and findIndex.
console.log('Find finds the value if the current logic')
console.log('FindINdex finds the index of the current logic')

// Use find to find the first country containing only six letters in the countries array
const CountryWith6Letters = countries.find(country => country.length === 6)
console.log(CountryWith6Letters)


// Use findIndex to find the position of the first country containing only six letters in the countries array
const CountryIndexWith6Letters = countries.findIndex(country => country.length === 6)
console.log(CountryIndexWith6Letters)

// Use findIndex to find the position of Norway if it doesn't exist in the array you will get -1.
const norwayIndex = countries.findIndex(country => country === 'Norway') // return -1 if not found
console.log(norwayIndex)

// Use findIndex to find the position of Russia if it doesn't exist in the array you will get -1.
const russiaIndex = countries.findIndex(country => country === 'Russia') // return -1 if not found
console.log(russiaIndex)


console.log("LEVEL 2")

// Find the total price of products by chaining two or more array iterators(eg. arr.map(callback).filter(callback).reduce(callback))

const totalPrice = products.map(product => product.price).filter(product => typeof product == 'number').reduce((acc,curr) => acc += curr)
console.log(totalPrice)

// Find the sum of price of products using only reduce(callback))
const totalPriceWithReduce = products.reduce((acc,curr) => {
    if (typeof curr.price === 'number'){
        acc += curr.price
    }
    return acc 
},0)
console.log(totalPriceWithReduce)

// Declare a function called categorizeCountries which returns an array of countries which have some common pattern(you find the countries array in this repository as countries.js(eg 'land', 'ia', 'island','stan')).


/*

Create a function which return an array of objects, which is the letter and the number of times the letter use to start with a name of a country.
Declare a getFirstTenCountries function and return an array of ten countries. Use different functional programming to work on the countries.js array
Declare a getLastTenCountries function which which returns the last ten countries in the countries array.
Find out which letter is used many times as initial for a country name from the countries array (eg. Finland, Fiji, France etc)
Exercises: Level 3
Use the countries information, in the data folder. Sort countries by name, by capital, by population

*** Find the 10 most spoken languages:

// Your output should look like this
console.log(mostSpokenLanguages(countries, 10))
[
{country: 'English',count:91},
{country: 'French',count:45},
{country: 'Arabic',count:25},
{country: 'Spanish',count:24},
{country:'Russian',count:9},
{country:'Portuguese', count:9},
{country:'Dutch',count:8},
{country:'German',count:7},
{country:'Chinese',count:5},
{country:'Swahili',count:4}
]

// Your output should look like this
console.log(mostSpokenLanguages(countries, 3))
[
{country: 'English',count: 91},
{country: 'French',count: 45},
{country: 'Arabic',count: 25},
]```
*** Use countries_data.js file create a function which create the ten most populated countries

console.log(mostPopulatedCountries(countries, 10))

[
{country: 'China', population: 1377422166},
{country: 'India', population: 1295210000},
{country: 'United States of America', population: 323947000},
{country: 'Indonesia', population: 258705000},
{country: 'Brazil', population: 206135893},
{country: 'Pakistan', population: 194125062},
{country: 'Nigeria', population: 186988000},
{country: 'Bangladesh', population: 161006790},
{country: 'Russian Federation', population: 146599183},
{country: 'Japan', population: 126960000}
]

console.log(mostPopulatedCountries(countries, 3))
[
{country: 'China', population: 1377422166},
{country: 'India', population: 1295210000},
{country: 'United States of America', population: 323947000}
]
```
*** Try to develop a program which calculate measure of central tendency of a sample(mean, median, mode) and measure of variability(range, variance, standard deviation). In addition to those measures find the min, max, count, percentile, and frequency distribution of the sample. You can create an object called statistics and create all the functions which do statistical calculations as method for the statistics object. Check the output below.

const ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

console.log('Count:', statistics.count()) // 25
console.log('Sum: ', statistics.sum()) // 744
console.log('Min: ', statistics.min()) // 24
console.log('Max: ', statistics.max()) // 38
console.log('Range: ', statistics.range() // 14
console.log('Mean: ', statistics.mean()) // 30
console.log('Median: ',statistics.median()) // 29
console.log('Mode: ', statistics.mode()) // {'mode': 26, 'count': 5}
console.log('Variance: ',statistics.var()) // 17.5
console.log('Standard Deviation: ', statistics.std()) // 4.2
console.log('Variance: ',statistics.var()) // 17.5
console.log('Frequency Distribution: ',statistics.freqDist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
console.log(statistics.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

*/