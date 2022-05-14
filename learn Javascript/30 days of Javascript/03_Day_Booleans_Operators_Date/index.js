console.log('LEVEL 1')

// Declare firstName, lastName, country, city, age, isMarried, year variable and assign value to it and use the typeof operator to check different data types.
let firstName = 'Shaswat'
let lastName = 'Singh'
let country = 'India'
let city = 'Pune'
let isMarried = false
let year = 2022

console.log(typeof(firstName))
console.log(typeof(lastName))
console.log(typeof(country))
console.log(typeof(isMarried))
console.log(typeof(city))
console.log(typeof(year))

// Check if type of '10' is equal to 10
console.log('10' === 10)

// Check if parseInt('9.8') is equal to 10
console.log(parseInt('9.8') == 10)

// Boolean value is either true or false.
let a = true
let b = false
// above two are boolean values

// Write three JavaScript statement which provide truthy value.
console.log(1 == true)
console.log(undefined == null)
console.log(3 !== '3')

// Write three JavaScript statement which provide falsy value.
console.log(NaN == NaN)
console.log(undefined === null)
console.log(0 === false)


// Figure out the result of the following comparison expression first without using console.log(). After you decide the result confirm it using console.log()

console.log(4 > 3 )    // true
console.log(4 >= 3 )   // true
console.log(4 < 3 )    // false
console.log(4 <= 3 )   // false
console.log(4 == 4 )   // true
console.log(4 === 4)   // true
console.log(4 != 4 )   // false
console.log(4 !== 4 )  // false
console.log(4 != '4')  // false
console.log(4 == '4' ) // true
console.log(4 === '4') // false

// Find the length of python and jargon and make a falsy comparison statement.
let lang1 = 'python'
let lang2 = 'jargon'
console.log(lang1.length != lang2.length)

// Figure out the result of the following expressions first without using console.log(). After you decide the result confirm it by using console.log()

console.log(4 > 3 && 10 < 12)    //true
console.log(4 > 3 && 10 > 12 )   //false
console.log(4 > 3 || 10 < 12 )   //true
console.log(4 > 3 || 10 > 12 )   //true
console.log(!(4 > 3)        )    //false
console.log(!(4 < 3)       )     //true
console.log(!(false)      )      //true
console.log(!(4 > 3 && 10 < 12)) //false
console.log(!(4 > 3 && 10 > 12)) //true
console.log(!(4 === '4')   )     //true

// Use the Date object to do the following activities

let now = new Date();
// What is the year today?
console.log(now.getFullYear())

// What is the month today as a number?
console.log(now.getMonth()+1)

// What is the date today?
console.log(now.getDate())

// What is the day today as a number?
console.log(now.getDay())

// What is the hours now?
console.log(now.getHours())

// What is the minutes now?
console.log(now.getMinutes())

// Find out the numbers of seconds elapsed from January 1, 1970 to now.
console.log(now.getTime())

console.log('LEVEL 2')

// Write a script that prompt the user to enter base and height of the triangle and calculate an area of a triangle (area = 0.5 x b x h).
let base = prompt('Enter the base of triangle','enter here')
let height = prompt('Enter the height of triangle','enter here')
console.log(.5*base *height)

// Write a script that prompt the user to enter side a, side b, and side c of the triangle and and calculate the perimeter of triangle (perimeter = a + b + c)
let x = parseInt(prompt('enter side'))
let y = parseInt(prompt('enter side'))
let z = parseInt(prompt('enter side'))
console.log(x+y+z)

// Compare your first name length and your family name length and you should get this output.
firstName = prompt('firstname')
lastName = prompt('last name')

firstName.length > lastName.length ? console.log(`Your first name,${firstName} is longer than your family name, ${lastName}`) : console.log(`Your first name,${firstName} is smaller than your family name, ${lastName}`)


console.log('LEVEL 3')

// Create a human readable time format using the Date time object. The hour and the minute should be all the time two digits(7 hours should be 07 and 5 minutes should be 05 )
// YYY-MM-DD HH:mm eg. 20120-01-02 07:05
now = new Date()
console.log(now)
year = now.getFullYear()
let month = now.getMonth()+1
if (month < 10){
    month = '0'+month
}
let currDate = now.getDate()
if (currDate < 10){
    currDate = '0'+currDate
}

let hour = now.getHours()
if (hour < 10){
    hour = '0'+hour
}

let minute  = now.getMinutes()
if (minute < 10){
    minute = '0'+minute
}
console.log(`${year}-${month}-${currDate} ${hour}:${minute}`)

