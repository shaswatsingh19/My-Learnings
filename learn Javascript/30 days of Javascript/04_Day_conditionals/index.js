
console.log('LEVEL 1')

// Get user input using prompt(“Enter your age:”). If user is 18 or older , give feedback:'You are old enough to drive' but if not 18 give another feedback stating to wait for the number of years he needs to turn 18.
let age = prompt("Enter your age")
if (age >= 18 ){
    console.log('You are old enough to drive');
}
else{
    console.log(`You have to wait for ${18-age} to needs to turn 18`)
}

// Compare the values of myAge and yourAge using if … else. Based on the comparison and log the result to console stating who is older (me or you). Use prompt(“Enter your age:”) to get the age as input.
let myAge = prompt('My age')
let yourAge = prompt('Your age')
if (myAge > yourAge ){
    console.log('I am older than you')
} else {
    console.log('Your are older than me')
}

let a = 5
let b = 2
a>b ? console.log(`${a} is greater than ${b}`) : console.log(`${b} is greater than ${a}`)


let num = prompt('Enter your number')
if (num % 2 == 0){
    console.log('EVEN')
} else{
    console.log('ODD')
}

console.log('LEVEL 2')


// Write a code which can give grades to students according to theirs scores:
// 90-100, A
// 70-89, B
// 60-69, C
// 50-59, D
// 0-49, F

let score = prompt('Enter your score')
if (score >= 90 && score <=100 ){
    console.log('A')
}else if(score >= 70 && score <=89 ){
    console.log('B')
}else if(score >= 60 && score <=69 ){
    console.log('C')
}else if(score >= 50 && score <=59 ){
    console.log('D')
}else if(score >= 0 && score <=49 ){
    console.log('E')
}

month = prompt('Enter the month')

switch (month){
    case 'September':
    case 'October':
    case 'November':
        console.log('Autumn');
        break;
    case 'December':
    case 'January':
    case 'February':
        console.log('Winter');
        break;
    case 'March':
    case 'May':
    case 'April':
        console.log('Spring');
        break;
    case 'June':
    case 'July':
    case 'August':
        console.log('Summer');  
}

/*
Check if a day is weekend day or a working day. Your script will take day as an input.
    What is the day  today? Saturday
    Saturday is a weekend.

    What is the day today? saturDaY
    Saturday is a weekend.

    What is the day today? Friday
    Friday is a working day.

    What is the day today? FrIDAy
    Friday is a working day.
 */
console.log('What is the day today? ')
let day = prompt('Today\'s Day')
console.log(day)
switch (day.toLowerCase()){
    case 'sunday':
        console.log(`Sunday is a weekend.`)
        break;
    case 'saturday':
        console.log(`Saturday is a weekend.`)
        break;
    case 'friday':
        console.log(`Friday is a weekday.`)
        break;
    case 'thursday':
        console.log(`Thursday is a weekday.`)
        break;
    case 'wednesday':
        console.log(`Wednesday is a weekday.`)
        break;
    case 'tuesday':
        console.log(`Tuesday is a weekday.`)
        break;
    case 'monday':
        console.log(`Monday is a weekday.`)
        break;
}

// console.log('LEVEL 3')

// Write a program which tells the number of days in a month,consider leap year.

/*    
  Enter a month: January
  January has 31 days.

  Enter a month: JANUARY
  January has 31 day

  Enter a month: February
  February has 28 days.

  Enter a month: FEbruary
  February has 28 days.
*/

console.log('Enter a month: ');
let month = prompt('Enter month')
switch(month.toLowerCase()){
    case 'january':
    case 'march':
    case 'may':
    case 'july':
    case 'August':
    case 'october':
    case 'december':
        console.log(`${month[0].toUpperCase()}${month.substring(1).toLowerCase()} has 31 days`)
        break;
    case 'september':
    case 'april':
    case 'june':
    case 'november':
        console.log(`${month[0].toUpperCase()}${month.substring(1).toLowerCase()} has 30 days`)
        break;
    case 'february':
        console.log(`${month[0].toUpperCase()}${month.substring(1).toLowerCase()} has 28 days`)
        break;
    default:
        console.log('You enter wrong month')
        
        

}