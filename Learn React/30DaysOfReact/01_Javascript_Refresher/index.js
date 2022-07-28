// console.log("ARRAY ")
// console.log("Exercis 1")



// //   Declare an empty array;

// const arr = []

// //   Declare an array with more than 5 number of elements

// let num  = [1,2,3,4,5]

// //   Find the length of your array

// console.log(num.length)

// //   Get the first item, the middle item and the last item of the array

// console.log(num[0],num[parseInt((num.length)/2)] ,  num[num.length-1])

// //   Declare an array called mixedDataTypes, put different data types in the array and find the length of the array. The array size should be greater than 5
// let mixedDataTypes = [1,'fs','c' ,function f(){console.log('s')} , {
//     'name':'shaswat',
//     'age':23,
// }]

// //   Declare an array variable name itCompanies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon

// const itCompanies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

// //   Print the array using console.log()
// console.log(itCompanies)

// //   Print the number of companies in the array
// console.log('The number of companies is ',itCompanies.length)

// //   Print the first company, middle and last company
// console.log('the first company is',itCompanies[0])

// console.log('the middle company is ',itCompanies[parseInt((itCompanies.length)/2)])
// console.log('the last company is ',itCompanies[itCompanies.length-1])


// //   Print out each company

// itCompanies.forEach( company => console.log(company))

// //   Change each company name to uppercase one by one and print them out

// itCompanies.map( company => console.log(company.toUpperCase()))

// //   Print the array like as a sentence: Facebook, Google, Microsoft, Apple, IBM,Oracle and Amazon are big IT companies.

// console.log(itCompanies.join(', ') + 'are big IT companies.')

// //   Check if a certain company exists in the itCompanies array. If it exist return the company else return a company is not found

// let companyToCheck = 'TCS'
// console.log('Checking for',companyToCheck,'that it exist in itCompanies or not ', itCompanies.includes(companyToCheck))

// //   Filter out companies which have more than one 'o' without the filter method

// console.log('Companies with more than 1 o are: ')
// itCompanies.forEach((company) => {
//     if (company.indexOf('o') != company.lastIndexOf('o')){
//         console.log(company)
//     }
// })

// //   Sort the array using sort() method
// console.log(itCompanies.sort())

// //   Reverse the array using reverse() method
// console.log('Reversing',itCompanies.reverse())

// //   Slice out the first 3 companies from the array
// console.log('slicing out first 3',itCompanies.slice(0,3))
// //   Slice out the last 3 companies from the array

// console.log('slicing out last 3',itCompanies.slice(itCompanies.length-3,))

// //   Slice out the middle IT company or companies from the array
// let mid = parseInt(itCompanies.length/2)
// console.log('SLice out the middle ', itCompanies.slice(mid,mid+3))

// //   Remove the first IT company from the array

// console.log(itCompanies.splice(0,3))

// //   Remove all IT companies

// console.log(itCompanies.splice(0,))


// console.log('Exercise 2 ')

// console.log(countries)
// console.log(webTechs)



// Destructuring object 

const props = {
    user:{
      firstName:'Asabeneh',
      lastName:'Yetayeh',
      age:250
    },
    post:{
      title:'Destructuring and Spread',
      subtitle:'ES6',
      year:2020
  },
  skills:['JS', 'React', 'Redux', 'Node', 'Python']
}



// const {user , post , skills } = props
// const {firstName , lastName , age } = user
// const [skills1 , skills2 , skills3]  = skills

// console.log(skills3)

// But we can destructure it in one step 

const {user:{firstName, lastName, age}, post:{title, subtitle, year}, skills:[skillOne, skillTwo, skillThree, skillFour, skillFive]} = props

