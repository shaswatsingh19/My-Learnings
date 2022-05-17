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

//   Declare an empty array;
let arr = Array()

// Declare an array with more than 5 number of elements
let array = Array(5)

// Find the length of your array
console.log(array.length)

// Get the first item, the middle item and the last item of the array
let firstItem = webTechs[0]

const mid = parseInt(webTechs.length/2)
let middleItem = webTechs[mid]

let lastItem = webTechs[webTechs.length-1]

// Declare an array called mixedDataTypes, put different data types in the array and find the length of the array. The array size should be greater than 5

let mixedDataTypes = [1,'A','spp',55.3,
    ['array','object'], 
    {
    'name':'shaswat',
    'age':23
    }
]
console.log(mixedDataTypes.length)

// Declare an array variable name itCompanies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon

let itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle','Amazon']

// Print the array using console.log()
console.log(itCompanies)

// Print the number of companies in the array
console.log(itCompanies.length)


// Print the first company, middle and last company
let firstCompany = itCompanies[0]

let middleCompany = itCompanies[parseInt(itCompanies.length/2)]

let lastCompany = itCompanies[itCompanies.length-1]

// Print out each company
for (let index = 0; index < itCompanies.length; index++) {
    console.log(itCompanies[index])
}

// Change each company name to uppercase one by one and print them out
for (let index = 0; index < itCompanies.length; index++) {
    console.log(itCompanies[index].toUpperCase())
}

// Print the array like as a sentence: Facebook, Google, Microsoft, Apple, IBM,Oracle and Amazon are big IT companies.

let allCompanies = itCompanies.join(', ')
console.log(allCompanies,' are big IT companies')

// Check if a certain company exists in the itCompanies array. If it exist return the company else return a company is not found

let checkForCompany = 'AT&T'
itCompanies.includes(checkForCompany) ? console.log(checkForCompany) : console.log('Companies is not found')

// Filter out companies which have more than one 'o' without the filter method
let companiesIncludesO = Array()
for (let index = 0; index < itCompanies.length; index++) {
    
    if ( itCompanies[index].toLowerCase().includes('o') ){
        companiesIncludesO.push(itCompanies[index])
    }
}

// itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
// Sort the array using sort() method
const sortedItCompanies = itCompanies.sort()
// itCompanies = ['Amazon', 'Apple', 'Facebook', 'Google', 'IBM', 'Microsoft', 'Oracle']


// Reverse the array using reverse() method
const reversedItCompanies = itCompanies.reverse()
// itCompanies = ['Oracle', 'Microsoft', 'IBM', 'Google', 'Facebook', 'Apple', 'Amazon']

// Slice out the first 3 companies from the array
// Slice out the last 3 companies from the array
// Slice out the middle IT company or companies from the array
const first3Companies = itCompanies.slice(0,3)
const last3Companies = itCompanies.slice(itCompanies.length-3,)

// Remove the first IT company from the array
let removedFirst = itCompanies.shift()

// Remove the middle IT company or companies from the array
let midd = parseInt(itCompanies.length / 2)
let startingMidCompanies = itCompanies.splice(midd)
startingMidCompanies = ['Facebook', 'Apple', 'Amazon']
itCompanies = ['Microsoft', 'IBM','Google']
itCompanies.pop() // removed last element of it companies
itCompanies =  itCompanies.concat(startingMidCompanies)

itCompanies =  ['Microsoft', 'IBM', 'Facebook', 'Apple', 'Amazon'] // google has been removed

// Remove the last IT company from the array
let removeLast = itCompanies.pop()

// Remove all IT companies
itCompanies = itCompanies.splice()

console.log('LEVEL 2')

/*
Create a separate countries.js file and store the countries array in to this file, create a separate file web_techs.js and store the webTechs array in to this file. Access both file in main.js file

import {webTechs} from 'webTechs.js'

console.log(webTechs)

First remove all the punctuations and change the string to array and count the number of words in the array

let text = 'I love teaching and empowering people. I teach HTML, CSS, JS, React, Python.'

let splittedArray = text.split(' ')
console.log(splittedArray.length)

console.log(words)
console.log(words.length)
["I", "love", "teaching", "and", "empowering", "people", "I", "teach", "HTML", "CSS", "JS", "React", "Python"]

*/


// In the following shopping cart add, remove, edit items

const shoppingCart = ['Milk', 'Coffee', 'Tea', 'Honey']

// add 'Meat' in the beginning of your shopping cart if it has not been already added

if ( !shoppingCart.includes('Meat') ){
    shoppingCart.unshift('Meat')
}

// add Sugar at the end of you shopping cart if it has not been already added

if ( !shoppingCart.includes('Sugar') ){
    shoppingCart.unshift('Sugar')
}

// remove 'Honey' if you are allergic to honey
const allergicToHoney  = true
if (allergicToHoney) shoppingCart.pop()


const indexOfTea = shoppingCart.indexOf('Tea')

// modify Tea to 'Green Tea'1
shoppingCart[indexOfTea] = 'Green Tea'

// In countries array check if 'Ethiopia' exists in the array if it exists print 'ETHIOPIA'. If it does not exist add to the countries list.

countries.includes('Ethiopia') ? console.log('ETHIOPIA') : countries.push('Ethiopia')

// In the webTechs array check if Sass exists in the array and if it exists print 'Sass is a CSS preprocess'. If it does not exist add Sass to the array and print the array.

webTechs.includes('Sass') ? console.log('Sass is a CSS preprocess') : webTechs.push('Sass')
console.log(webTechs)

// Concatenate the following two variables and store it in a fullStack variable.

const frontEnd = ['HTML', 'CSS', 'JS', 'React', 'Redux']
const backEnd = ['Node','Express', 'MongoDB']

const fullStack = frontEnd.concat(backEnd)
console.log(fullStack)


console.log('LEVEL 3')

// The following is an array of 10 students ages:
// Sort the array and find the min and max age
const ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()

const min = ages[0]
const max = ages[ages.length -1]

// Find the median age(one middle item or two middle items divided by two)

let median  = (ages[4] + ages[5])/2

// Find the average age(all items divided by number of items)

let sum = 0
for (let i=0;i<ages.length;i++){
    sum += ages[i]
    
}
const avg  = sum/ages.length
console.log(avg)

// Find the range of the ages(max minus min)
const range = max  - min
console.log(range)

// Compare the value of (min - average) and (max - average), use abs() method 
console.log( Math.abs(min-avg) > Math.abs(avg-max) )

