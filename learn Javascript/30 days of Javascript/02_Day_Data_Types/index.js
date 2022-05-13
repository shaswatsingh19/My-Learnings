console.log('13-05-2022')
console.log('EXERCISE 2')

console.log('LEVEL 1')

// Declare a variable named challenge and assign it to an initial value '30 Days Of JavaScript'.
const challenge = '30 Days of Javascript'

// Print the string on the browser console using console.log()
console.log(challenge)

// Print the length of the string on the browser console using console.log()
console.log(challenge.length)

// Change all the string characters to capital letters using toUpperCase() method
console.log(challenge.toUpperCase())

// Change all the string characters to lowercase letters using toLowerCase() method
console.log(challenge.toLowerCase())

// Cut (slice) out the first word of the string using substr() or substring() method
console.log(challenge.substr(0,2))

// Slice out the phrase Days Of JavaScript from 30 Days Of JavaScript.
console.log(challenge.substring(3,challenge.length))

// Check if the string contains a word Script using includes() method
console.log(challenge.includes('Script'))  // includes does not check for case sensitive 

// Split the string into an array using split() method
console.log(challenge.split())

// Split the string 30 Days Of JavaScript at the space using split() method
console.log(challenge.split(' '))


// 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' split the string at the comma and change it to an array.
let companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
console.log(companies.split(', '))

// Change 30 Days Of JavaScript to 30 Days Of Python using replace() method.
console.log(challenge.replace('Javascript','Python'))

// What is character at index 15 in '30 Days Of JavaScript' string? Use charAt() method.
console.log(challenge.charAt(15))

// What is the character code of J in '30 Days Of JavaScript' string using charCodeAt()
console.log(challenge.charCodeAt(challenge.indexOf('J')))

// Use indexOf to determine the position of the first occurrence of a in 30 Days Of JavaScript
console.log(challenge.indexOf('a'))

// Use lastIndexOf to determine the position of the last occurrence of a in 30 Days Of JavaScript.
console.log(challenge.lastIndexOf('a'))

// Use indexOf to find the position of the first occurrence of the word because in the following sentence:
let sentence = 'You cannot end a sentence with because because because is a conjunction'
console.log(sentence.indexOf('because'))

// Use lastIndexOf to find the position of the last occurrence of the word because in the above sentence
console.log(sentence.lastIndexOf('because'))

// Use search to find the position of the first occurrence of the word because in the above sentence
console.log(sentence.search('because'))

// Use trim() to remove any trailing whitespace at the beginning and the end of a string.E.g ' 30 Days Of JavaScript '.
let challenge2 = ' 30 Days Of JavaScript '
console.log(challenge2.trim())

// Use startsWith() method with the string 30 Days Of JavaScript and make the result true
console.log(challenge.startsWith('30')) 

// Use endsWith() method with the string 30 Days Of JavaScript and make the result true
console.log(challenge.endsWith('script'))

// Use match() method to find all the a’s in 30 Days Of JavaScript
let pattern = /a/gi // g means to check whole string and i means for case insensitive 
console.log(challenge.match(pattern))

// Use concat() and merge '30 Days of' and 'JavaScript' to a single string, '30 Days Of JavaScript'
let first = '30 Days of '
let second= 'Javascript'
first = first.concat(second)
console.log(first)

// Use repeat() method to print 30 Days Of JavaScript 2 times
console.log(challenge.repeat(3))


console.log('LEVEL 2')

console.log("The quote 'There is no exercise better for the heart than reaching down and lifting people up.' by John Holmes teaches us to help one another.")

console.log('"Love is not patronizing and charity isn\'t about pity, it is about love. Charity and love are the same -- with charity you give love, so don\'t just give money but reach out your hand instead."')

// Check if typeof '10' is exactly equal to 10. If not make it exactly equal.'
let n1 = '10'
let n2 = 10
console.log(typeof(n1) == typeof(n2))
console.log(typeof(parseInt(n1)) == typeof(n2))

// Check if parseFloat('9.8') is equal to 10 if not make it exactly equal with 10.
const a = '9.8'
const b = 10
console.log(parseFloat(a) == b)
console.log(Math.round(parseFloat(a)) == b)


// Check if 'on' is found in both python and jargon
const str1 = 'python'
const str2 = 'jargon'
console.log(str1.includes('on'))
console.log(str2.includes('on'))

// I hope this course is not full of jargon. Check if jargon is in the sentence.
sentence = 'I hope this course is not full of jargon'
console.log(sentence.includes('jargon'))

// Generate a random number between 0 and 100 inclusively.
let randNumber = Math.round(Math.random()*101)
console.log(randNumber)

// Generate a random number between 50 and 100 inclusively.
randNumber  = Math.round(Math.random()*(100-50))+50  
console.log(randNumber)

// Generate a random number between 0 and 255 inclusively.
randNumber  = Math.round(Math.random()*(256))  
console.log(randNumber)

// Access the 'JavaScript' string characters using a random number.
let string = 'Javascript'
console.log(string.charAt(Math.round(Math.random()*string.length-1)))

/*
Use console.log() and escape characters to print the following pattern.

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
*/
console.log('1 1 1 1 1\n2 1 2 4 8\n3 1 3 9 27\n4 1 4 16 64\n5 1 5 25 125')


// Use substr to slice out the phrase because because because from the following sentence:
sentence ='You cannot end a sentence with because because because is a conjunction'

let startIndex = sentence.indexOf('because') //31
let lastIndex = sentence.lastIndexOf('because') //47
let ans = sentence.substr(startIndex,lastIndex-startIndex+'because'.length)
console.log(ans)


console.log('LEVEL 3')


//Count the number of word love in this sentence.
let word  = 'Love is the best thing in this world. Some found their love and some are still looking for their love.'
pattern = /love/gi
let count = word.match(pattern)
console.log(count.length)


// Use match() to count the number of all because in the following sentence 
sentence ='You cannot end a sentence with because because because is a conjunction'
pattern = /because/gi
count = sentence.match(pattern)
console.log(count.length)

// Clean the following text and find the most frequent word (hint, use replace and regular expressions).

sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %te@a@ching%;. The@re $is no@th@ing; &as& mo@re rewarding as educa@ting &and& @emp%o@weri@ng peo@ple. ;I found tea@ching m%o@re interesting tha@n any ot#her %jo@bs. %Do@es thi%s mo@tiv#ate yo@u to be a tea@cher!? %Th#is 30#Days&OfJavaScript &is al@so $the $resu@lt of &love& of tea&ching'

console.log(sentence.replace(/[!@#$%^&?;]/g,""))

// Calculate the total annual income of the person by extracting the numbers from the following text.
sentence = 'He earns 5000 euro from salary per month, 10000 euro annual bonus, 15000 euro online courses per month.'

pattern  = /\d+/g
const income  = sentence.match(pattern)
console.log(income)
let totalAnnualIncome = parseInt(income[0]*12) + parseInt(income[1]) + parseInt(income[2]*12)
console.log(totalAnnualIncome)