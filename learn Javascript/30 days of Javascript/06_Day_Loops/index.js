console.log('LEVEL 1')

const countries = [
    'Germany',
    'Canada',
    'Albania',
    'Ireland',
    'Bolivia',
    'Ethiopia',
    'Denmark',
    'Hungary',
    'Finland',
    'Japan',
    'Kenya'
]
  const webTechs = [
    'HTML',
    'CSS',
    'JavaScript',
    'React',
    'Redux',
    'Node',
    'MongoDB'
  ]
  const mernStack = ['MongoDB', 'Express', 'React', 'Node']

//   Iterate 0 to 10 using for loop, do the same using while and do while loop
for(let i=0 ;i<10;i++){
    console.log(i)
}

let i=0
while(i<10){
    console.log(i)
    i+=1
}
// Iterate 10 to 0 using for loop, do the same using while and do while loop


for(i=10;i>-1;i--){
    console.log(i)
}

i=10
while(i>-1){
    console.log(i)
    i-=1
}

// Iterate 0 to n using for loop
// const n = prompt('Enter a number')
// for (i=0;i<n;i++){
//     console.log(i)
// }

// Write a loop that makes the following pattern using console.log():

let pattern = '#'
for (i = 1;i<6;i++){
    console.log(pattern)
    pattern += '#'
}

// Use loop to print the following pattern:
    // 0 x 0 = 0
    // 1 x 1 = 1
    // 2 x 2 = 4
    // 3 x 3 = 9
    // 4 x 4 = 16
    // 5 x 5 = 25
    // 6 x 6 = 36
    // 7 x 7 = 49
    // 8 x 8 = 64
    // 9 x 9 = 81
    //   10 x 10 = 100
for (i=0;i<11;i++){
    console.log(`${i} * ${i} = ${i * i}`)
}

// Using loop print the following pattern

//  i    i^2   i^3
//  0    0     0
//  1    1     1
//  2    4     8
//  3    9     27
//  4    16    64
//  5    25    125
//  6    36    216
//  7    49    343
//  8    64    512
//  9    81    729
//  10   100   1000

console.log('i   i^2   i^3')
for (i=0;i<11;i++){
    console.log(`${i}   ${i**2}   ${i**3}`)
}

// Use for loop to iterate from 0 to 100 and print only even numbers
for (i=0;i<101;i+=2){
    console.log(i)
}

// Use for loop to iterate from 0 to 100 and print only odd numbers
for(i=1;i<101;i+=2){
    console.log(i)
}

// Use for loop to iterate from 0 to 100 and print only prime numbers
console.log('Primes till 100')
for (i =2;i<101;i++){
    let prime = true
    for (let j=2;j*j<=i;j++){
        if (i%j==0){
            prime = false
            break;
        }
    }
    if (prime){
        console.log(i)
    }
}
// Use for loop to iterate from 0 to 100 and print the sum of all numbers.
console.log('Sum till 100')
let sum = 0
for(i = 0;i<101;i++){
    sum += i
}
console.log(sum)

// Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
console.log('Sum of even and odd')
let sumOfEven = 0
let sumOfOdd  = 0
for(i=1;i<101;i++){
    if (i%2==0) sumOfEven += i
    else sumOfOdd += i
}

console.log(sumOfEven,sumOfOdd)

// Develop a small script which generate array of 5 random numbers
let randomNumberArray = []
i=0
while(i<5){
    const randomNum = Math.round(Math.random()*10)
    randomNumberArray.push(randomNum)
    i+=1
}
console.log(randomNumberArray)

// Develop a small script which generate array of 5 random numbers and the numbers must be unique
console.log('Unique Random Number')
let uniqueRandomNumber = []
i=0
while(i<5 && uniqueRandomNumber.length<5){
    const randomNum = Math.round(Math.random()*10)
    if ( !uniqueRandomNumber.includes(randomNum) ){
        uniqueRandomNumber.push(randomNum)
        i+=1
    }
    else{
        i-=1
    }
    
}
console.log(uniqueRandomNumber)

// Develop a small script which generate a six characters random id:
console.log('RANDOM ID')
pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
let res = ''

for (i=0;i<6;i++){
    const ind = Math.floor(Math.random()*pattern.length)
    res += pattern.charAt(ind)
    console.log(ind)
}
console.log(res)

console.log("LEVEL 2")

// Develop a small script which generate any number of characters random id:

console.log('RANDOM IDs of Random length')
pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
res = ''
let range  = Math.round(Math.random()*15)
for (i=0;i<range;i++){
    const ind = Math.floor(Math.random()*pattern.length)
    res += pattern.charAt(ind)
    console.log(ind)
}
console.log(res)

// Write a script which generates a random hexadecimal number.
const hexaPattern = '0123456789ABCDEF'
res = ''
range  = Math.round(Math.random()*20)
for (i=0;i<range;i++){
    const ind = Math.floor(Math.random()*hexaPattern.length)
    res += hexaPattern.charAt(ind)
    console.log(ind)
}
console.log(res)

// Write a script which generates a random rgb color number.
console.log('Random RGB generator')
let red = Math.floor(Math.random()*256)
let green = Math.floor(Math.random()*256)
let blue = Math.floor(Math.random()*256)

console.log(`rgb( ${red}, ${green}, ${blue} )`)

// Using the above countries array, create the following new array.
// ["ALBANIA", "BOLIVIA", "CANADA", "DENMARK", "ETHIOPIA", "FINLAND", "GERMANY", "HUNGARY", "IRELAND", "JAPAN", "KENYA"]


let countriesInUpperCase = []
for(i=0;i<countries.length;i++){
    countriesInUpperCase.push(countries[i].toUpperCase());
}
console.log(countriesInUpperCase)

// Using the above countries array, create an array for countries length'.
let countriesLength = []
for(i=0;i<countries.length;i++){
    countriesLength.push(countries[i].length);
}
console.log(countriesLength)

// Use the countries array to create the following array of arrays:

//   [
//   ['Albania', 'ALB', 7],
//   ['Bolivia', 'BOL', 7],
//   ['Canada', 'CAN', 6],
//   ['Denmark', 'DEN', 7],
//   ['Ethiopia', 'ETH', 8],
//   ['Finland', 'FIN', 7],
//   ['Germany', 'GER', 7],
//   ['Hungary', 'HUN', 7],
//   ['Ireland', 'IRE', 7],
//   ['Iceland', 'ICE', 7],
//   ['Japan', 'JAP', 5],
//   ['Kenya', 'KEN', 5]
// ]

let codedCountryList = []
for(i=0;i<countries.length;i++){
    const coded = [countries[i], countriesInUpperCase[i].substring(0,3) , countriesLength[i] ]
    codedCountryList.push(coded)
}
console.log(codedCountryList)
for(let arr of codedCountryList){
    console.log(arr)
}

// In above countries array, check if there is a country or countries containing the word 'land'. If there are countries containing 'land', print it as array. If there is no country containing the word 'land', print 'All these countries are without land'.
console.log('Countries containing land in there word')
let countriesContainingLand  = []
for(i=0;i<countries.length;i++){
    
    if(countries[i].includes('land')){
        countriesContainingLand.push(countries[i])
    }
}
if (countriesContainingLand.length > 0) {
    console.log(countriesContainingLand)
}
else{
    console.log('All these countries are without land')
}
// In above countries array, check if there is a country or countries end with a substring 'ia'. If there are countries end with, print it as array. If there is no country containing the word 'ai', print 'These are countries ends without ia'.

console.log('countries ends with ia')
let countriesContainingIA = []
let hasIA = false
for (let country of countries){
    if (country.endsWith('ia')){
        countriesContainingIA.push(country)
        hasIA  = true
    }
}
if (hasIA){
    console.log(countriesContainingIA)
}
else{
    console.log('These are countries ends without ia')   
}

// Using the above countries array, find the country containing the biggest number of characters.
console.log('country containing the biggest number of characters')
let biggestCountryName = ''
let lengthOfBiggestCountry = 0
for(i=0;i<countriesLength.length;i++){
    if ( countriesLength[i] > lengthOfBiggestCountry){
        lengthOfBiggestCountry = countriesLength[i]
        biggestCountryName = countries[i]
    }
}
console.log(biggestCountryName)

// Using the above countries array, find the country containing only 5 characters.
console.log('country containing only 5 characters')
let countryWith5Character = []
for(i=0;i<countriesLength.length;i++){
    if ( countriesLength[i] ===  5){
        
        countryWith5Character.push(countries[i])
    }
}
console.log(countryWith5Character)

// Find the longest word in the webTechs array
console.log('longest word in the webTechs array')
let longestWord = ''
let lengthOfLongestWord = 0
for(i=0;i<webTechs.length;i++){
    if ( webTechs[i].length > lengthOfLongestWord){
        longestWord = webTechs[i]
        lengthOfLongestWord = webTechs[i].length
    }
}
console.log(longestWord)

// Iterate through the array, ["HTML", "CSS", "JS", "React", "Redux", "Node", "Express", "MongoDB"] using a for loop or for of loop and print out the items.
console.log('USING FOR of loop')
for(let tech of webTechs){
    console.log(tech)
}

// This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop without using a reverse method.
console.log('Reverse Array without reverse function')
let fruits = ['banana', 'orange', 'mango', 'lemon']
let start = 0
let end = fruits.length - 1
while (start < end){
    const temp = fruits[start]
    fruits[start] = fruits[end]
    fruits[end] = temp
    start+=1
    end-=1
}

console.log(fruits)
// Print all the elements of array as shown below.

  const fullStack = [
    ['HTML', 'CSS', 'JS', 'React'],
    ['Node', 'Express', 'MongoDB']
  ]
//   HTML
//   CSS
//   JS
//   REACT
//   NODE
//   EXPRESS
//   MONGODB

for(i=0;i<fullStack.length;i++){
    for(let j=0;j<fullStack[i].length;j++){
        console.log(fullStack[i][j])
    }
}

console.log('LEVEL 3')

// Copy countries array(Avoid mutation)
// Arrays are mutable. Create a copy of array which does not modify the original. Sort the copied array and store in a variable sortedCountries

let sortedCountriesCopy = [...countries].sort() // spread operator create shallow copy

console.log(countries)
console.log(sortedCountriesCopy)

// Sort the webTechs array and mernStack array
console.log(webTechs.sort())
console.log(mernStack.sort())

// Reverse the countries array and capitalize each country and stored it as an array

console.log(countriesInUpperCase.reverse())