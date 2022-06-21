console.log('LEVEL 1')

// Calculate the total annual income of the person from the following text. 
let info = 'He earns 4000 euro from salary per month, 10000 euro annual bonus, 5500 euro online courses per month.'

let pattern = /\d+/g
let amount = info.match(pattern)
console.log(amount)
let total = amount.reduce((acc,curr) => {
    if (curr == '10000'){
      acc += parseInt(curr)
    }
    else{
      acc += parseInt(curr)*12
    }
    return acc
} , 0 )
console.log('Total Annual income is '+ total + ' euro')

// The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers and find the distance between the two furthest particles.
let text = 'The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

pattern = /-?\d+/g
let points = text.match(pattern)
console.log(points)
points  = points.map(el => parseInt(el))
let distance = points[points.length - 1 ] - points[0]
console.log(distance)


// Write a pattern which identify if a string is a valid JavaScript variable

let validPattern = /[_$]?^[a-zA-Z]+/g
// text = '$_-1'
console.log(text.match(pattern))

const is_valid_variable = text => {
  
  console.log(text)
  console.log(validPattern)
  return validPattern.test(text)

}

console.log(is_valid_variable('first_name')) // True
console.log(is_valid_variable('first-name') )//# False
console.log(is_valid_variable('1first_name'))// # False
console.log(is_valid_variable('firstname'))// # True
console.log(is_valid_variable('$firstname'))// # True
console.log(is_valid_variable('_firstname'))// # True

console.log('LEVEL 2')
/*

Write a function called tenMostFrequentWords which get the ten most frequent word from a string?

    paragraph = `I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.`
    console.log(tenMostFrequentWords(paragraph))
    [
    {word:'love', count:6},
    {word:'you', count:5},
    {word:'can', count:3},
    {word:'what', count:2},
    {word:'teaching', count:2},
    {word:'not', count:2},
    {word:'else', count:2},
    {word:'do', count:2},
    {word:'I', count:2},
    {word:'which', count:1},
    {word:'to', count:1},
    {word:'the', count:1},
    {word:'something', count:1},
    {word:'if', count:1},
    {word:'give', count:1},
    {word:'develop',count:1},
    {word:'capabilities',count:1},
    {word:'application', count:1},
    {word:'an',count:1},
    {word:'all',count:1},
    {word:'Python',count:1},
    {word:'If',count:1}]
console.log(tenMostFrequentWords(paragraph, 10))
[{word:'love', count:6},
{word:'you', count:5},
{word:'can', count:3},
{word:'what', count:2},
{word:'teaching', count:2},
{word:'not', count:2},
{word:'else', count:2},
{word:'do', count:2},
{word:'I', count:2},
{word:'which', count:1}
]
Exercises: Level 3
Writ a function which cleans text. Clean the following text. After cleaning, count three most frequent words in the string.
  sentence = `%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?`
  console.log(cleanText(sentence))
 I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
 ```
2. Write a function which find the most frequent words. After cleaning, count three most frequent words in the string.

```js
 console.log(mostFrequentWords(cleanedText))
 [{word:'I', count:3}, {word:'teaching', count:2}, {word:'teacher', count:2}]
 */