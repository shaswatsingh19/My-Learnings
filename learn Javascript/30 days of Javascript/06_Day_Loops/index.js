console.log('LEVEL 1')

const countries = [
    'Albania',
    'Bolivia',
    'Canada',
    'Denmark',
    'Ethiopia',
    'Finland',
    'Germany',
    'Hungary',
    'Ireland',
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

console.log('RANDOM ID')
pattern = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
res = ''
const range  = Math.round(Math.random()*15)
for (i=0;i<range;i++){
    const ind = Math.floor(Math.random()*pattern.length)
    res += pattern.charAt(ind)
    console.log(ind)
}
console.log(res)

/*
Write a script which generates a random hexadecimal number.

'#ee33df'
Write a script which generates a random rgb color number.

rgb(240,180,80)
Using the above countries array, create the following new array.

["ALBANIA", "BOLIVIA", "CANADA", "DENMARK", "ETHIOPIA", "FINLAND", "GERMANY", "HUNGARY", "IRELAND", "JAPAN", "KENYA"]
Using the above countries array, create an array for countries length'.

[7, 7, 6, 7, 8, 7, 7, 7, 7, 5, 5]
Use the countries array to create the following array of arrays:

  [
  ['Albania', 'ALB', 7],
  ['Bolivia', 'BOL', 7],
  ['Canada', 'CAN', 6],
  ['Denmark', 'DEN', 7],
  ['Ethiopia', 'ETH', 8],
  ['Finland', 'FIN', 7],
  ['Germany', 'GER', 7],
  ['Hungary', 'HUN', 7],
  ['Ireland', 'IRE', 7],
  ['Iceland', 'ICE', 7],
  ['Japan', 'JAP', 5],
  ['Kenya', 'KEN', 5]
]
In above countries array, check if there is a country or countries containing the word 'land'. If there are countries containing 'land', print it as array. If there is no country containing the word 'land', print 'All these countries are without land'.

['Finland','Ireland', 'Iceland']
In above countries array, check if there is a country or countries end with a substring 'ia'. If there are countries end with, print it as array. If there is no country containing the word 'ai', print 'These are countries ends without ia'.

['Albania', 'Bolivia','Ethiopia']
Using the above countries array, find the country containing the biggest number of characters.

Ethiopia
Using the above countries array, find the country containing only 5 characters.

['Japan', 'Kenya']
Find the longest word in the webTechs array

Use the webTechs array to create the following array of arrays:

[["HTML", 4], ["CSS", 3],["JavaScript", 10],["React", 5],["Redux", 5],["Node", 4],["MongoDB", 7]]
An application created using MongoDB, Express, React and Node is called a MERN stack app. Create the acronym MERN by using the array mernStack

Iterate through the array, ["HTML", "CSS", "JS", "React", "Redux", "Node", "Express", "MongoDB"] using a for loop or for of loop and print out the items.

This is a fruit array , ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop without using a reverse method.

Print all the elements of array as shown below.

  const fullStack = [
    ['HTML', 'CSS', 'JS', 'React'],
    ['Node', 'Express', 'MongoDB']
  ]
  HTML
  CSS
  JS
  REACT
  NODE
  EXPRESS
  MONGODB
 */