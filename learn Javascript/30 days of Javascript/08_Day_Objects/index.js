
// a = 1 // window global object can be accessed everywhere
// function learnScope(){
//     console.log(a)
//     if (true){
//         a = 99
//         console.log(a)
//     }
//     console.log(a)
// }
// console.log(a) 

// global scope 

// let a = 1 // window global object can be accessed everywhere
// function globalScope(){
//     console.log(a) // 1 global scope
//     if (true){
//         let a = 99 
//         console.log(a) // 99 as new value of a is 99 which is global to if block
//     }
//     console.log(a)  // 1 
// }
// globalScope()
// console.log(a)  // 1

                
console.log('LEVEL 1')

// Create an empty object called dog
// Print the the dog object on the console
// Add name, legs, color, age and bark properties for the dog object. The bark property is a method which return woof woof

const dog = {}
console.log(dog)

dog.name = 'Tiger'
dog.age = 3
dog.color = 'grey'
dog.legs = 4
dog.bark = function(){
    return 'woof woof'
}
// Get name, legs, color, age and bark value from the dog object
console.log(`${dog.name} is a dog who is ${dog.age} years old and has ${dog.color} color body who does ${dog.bark()}`)

// Set new properties the dog object: breed, getDogInfo

dog.breed = 'indian'

dog.getDogInfo = function(){
    return `${this.name} is a dog who is ${this.age} years old and has ${this.color} color body who does ${this.bark()}`
}

console.log(dog.getDogInfo())

console.log('Level 2')


const users = {
    Alex: {
        email: 'alex@alex.com',
        skills: ['HTML', 'CSS', 'JavaScript'],
        age: 20,
        isLoggedIn: false,
        points: 30
    },
    Asab: {
        email: 'asab@asab.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'Redux', 'MongoDB', 'Express', 'React', 'Node'],
        age: 25,
        isLoggedIn: false,
        points: 50
    },
    Brook: {
        email: 'daniel@daniel.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'React', 'Redux'],
        age: 30,
        isLoggedIn: true,
        points: 50
    },
    Daniel: {
        email: 'daniel@alex.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'Python'],
        age: 20,
        isLoggedIn: false,
        points: 40
    },
    John: {
        email: 'john@john.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'React', 'Redux', 'Node.js'],
        age: 20,
        isLoggedIn: true,
        points: 50
    },
    Thomas: {
        email: 'thomas@thomas.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'React'],
        age: 20,
        isLoggedIn: false,
        points: 40
    },
    Paul: {
        email: 'paul@paul.com',
        skills: ['HTML', 'CSS', 'JavaScript', 'MongoDB', 'Express', 'React', 'Node'],
        age: 20,
        isLoggedIn: false,
        points: 40
    }
}
// Find the person who has many skills in the users object.

let highestSkills = 0
let userWithHighestSkill = ''

for (let user of Object.keys(users)){
    const skillLength = users[user].skills.length // users['Paul'].skills.length = 7
    if ( skillLength > highestSkills){
        highestSkills = skillLength
        userWithHighestSkill = user
    }
}

console.log(userWithHighestSkill)

// Count logged in users, count users having greater than equal to 50 points from the following object.
const loggedInUser = []
let pointsGreaterThan50 = 0

for (let user of Object.keys(users)){
    
    if (users[user].isLoggedIn){
        loggedInUser.push(user)
    }
    if (users[user].points >= 50){
        pointsGreaterThan50 += 1
    }
}

console.log(loggedInUser)
console.log(pointsGreaterThan50)

// Find people who are MERN stack developer from the users object
const mernDeveloper = []
for (let user of Object.keys(users)){
    const skill = users[user].skills
    if (skill.includes('MongoDB') && skill.includes('Express') && skill.includes('React') && skill.includes('Node')){
        mernDeveloper.push(user)
    }
}

// // // // // // // // // Set your name in the users object without modifying the original users object
// // // // // // // // const copyUsers = Object.assign({},users)
// // // // // // // // console.log(copyUsers)

// ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
// *****************************

// Get all keys or properties of users object
console.log(Object.keys(users))

// Get all the values of users object

console.log(Object.values(users))

console.log('LEVEL 3')

// Create an object literal called personAccount. It has firstName, lastName, incomes, expenses properties and it has totalIncome, totalExpense, accountInfo,addIncome, addExpense and accountBalance methods. Incomes is a set of incomes and its description and expenses is a set of incomes and its description.

personAccount = {
    'firstName' : 'Shaswat',
    'lastName' : 'Singh',
    'income' : {
        'work' :450000,
        'pocket money':12000
    },
    'expenses':{
        'food':360000,
        'data':5000
    },
    'totalIncome' : function(){
        let values = Object.values(this.income)
        let tIncome = 0
        for (let i of values){
            tIncome += i
        }
        return tIncome
    },
    'totalExpenses' : function(){
        let values = Object.values(this.expenses)
        let tExpense = 0
        for (let i of values){
            tExpense += i
        }
        return tExpense
    },
    'addIncome' : function(job,pay){
        this.income[job] = pay
        
    },
    'addExpense' : function(expense,amount){
        this.expense[expense] = amount
    },
    'accountBalance' : function(){
        return this.totalIncome() - this.totalExpenses()
    },
    'accountInfo' : function(){
        return `name:${this.firstName} ${this.lastName} \nincomes:${Object.entries(this.income)} \nexpenses: ${Object.entries(this.expenses)} \ntotalIncome: ${this.totalIncome()} \ntotalExpenses: ${this.totalExpenses()}\naccountBalance: ${this.accountBalance()}
                `
    } 
}

console.log(personAccount.accountInfo())

const newUsers = [
    {
        _id: 'ab12ex',
        username: 'Alex',
        email: 'alex@alex.com',
        password: '123123',
        createdAt:'08/01/2020 9:00 AM',
        isLoggedIn: false
    },
    {
        _id: 'fg12cy',
        username: 'Asab',
        email: 'asab@asab.com',
        password: '123456',
        createdAt:'08/01/2020 9:30 AM',
        isLoggedIn: true
    },
    {
        _id: 'zwf8md',
        username: 'Brook',
        email: 'brook@brook.com',
        password: '123111',
        createdAt:'08/01/2020 9:45 AM',
        isLoggedIn: true
    },
    {
        _id: 'eefamr',
        username: 'Martha',
        email: 'martha@martha.com',
        password: '123222',
        createdAt:'08/01/2020 9:50 AM',
        isLoggedIn: false
    },
    {
        _id: 'ghderc',
        username: 'Thomas',
        email: 'thomas@thomas.com',
        password: '123333',
        createdAt:'08/01/2020 10:00 AM',
        isLoggedIn: false
    }
    ];


// Imagine you are getting the above users collection from a MongoDB database. 
// a. Create a function called signUp which allows user to add to the collection. If user exists, inform the user that he has already an account.
const signUp = (username, email, password) => {
    newUsers.forEach(user => {
        if (user.username === username && user.password === password) {
            console.log("you already have an account")
        } else {
            let date = new Date()
            let chars = "abcdefghiklmnopqrstuvwxyz";
            let id = [];
            for (let i = 0; i < 6; i++) {
                id.push(chars[Math.floor(Math.random() * chars.length)])
            }
            id = id.join("");
            newUsers.push({
                _id: id,
                username: username,
                email: email,
                password: password,
                createdAt: `${date.getDate()}/${date.getMonth()}/${date.getFullYear()} ${date.getHours()}:${date.getMinutes()}`,
                isLoggedIn: "false"
            })
        }
    })
    console.log(newUsers[newUsers.length - 1]);
}

signUp('shaswat','hello@wrk.in',12321)
console.log(newUsers)
// b. Create a function called signIn which allows user to sign in to the application
const signIn = (username, password) => {
    for (let i = 0; i < users.length; i++) {
        if (users[i].username.toLowerCase() === username.toLowerCase() && users[0].password === password) {
            return users[i];
        } else {
            return "wrong username or password";
        }
    }
    // console.log(foundUser)
}

const products = [
    {
      _id: 'eedfcf',
      name: 'mobile phone',
      description: 'Huawei Honor',
      price: 200,
      ratings: [
        { userId: 'fg12cy', rate: 5 },
        { userId: 'zwf8md', rate: 4.5 }
      ],
      likes: []
    },
    {
      _id: 'aegfal',
      name: 'Laptop',
      description: 'MacPro: System Darwin',
      price: 2500,
      ratings: [],
      likes: ['fg12cy']
    },
    {
      _id: 'hedfcg',
      name: 'TV',
      description: 'Smart TV:Procaster',
      price: 400,
      ratings: [{ userId: 'fg12cy', rate: 5 }],
      likes: ['fg12cy']
    }
  ]
  
// The products array has three elements and each of them has six properties. 
// a. Create a function called rateProduct which rates the product 

const rateProduct = function() {
    
    for (let i = 0;i<products.length;i++){

        const property = products[i].ratings
        const len = property.length
        let totalRating = 0
        
        for (let j=0 ; j<len ; j++){
            totalRating += property[j].rate
        }
        if (len > 0){
            products[i]['total_rating'] = totalRating/len
        }
        else{
            products[i]['total_rating']  = 'No Rating till Now'
        }
        console.log(products[i].name)
        console.log(products[i]['total_rating'])
    }
}
rateProduct()


// b. Create a function called averageRating which calculate the average rating of a product

// Create a function called likeProduct. This function will helps to like to the product if it is not liked and remove like if it was liked.
/*
    



*/