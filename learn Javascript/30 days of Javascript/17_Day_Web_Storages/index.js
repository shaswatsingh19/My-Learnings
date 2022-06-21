console.log('LEVEL 1')

// Store you first name, last name, age, country, city in your browser localStorage.

localStorage.setItem('firstName','Shaswat')
localStorage.setItem('lastName','Singh')
localStorage.setItem('age',21)
localStorage.setItem('country','India')
localStorage.setItem('city','Pune')

console.log('LEVEL 2')
// Create a student object. The student object will have first name, last name, age, skills, country, enrolled keys and values for the keys. Store the student object in your browser localStorage.

const student = {
    'firstName'  :'Shaswat',    
    'lastName'  :'Singh',  
    'age' :     21    ,
    'country': 'India'   ,
    'city' : 'Pune'   
}
const studentJSON = JSON.stringify(student)
localStorage.setItem('student' ,studentJSON)

console.log("LEVEL 3")


// Create an object called personAccount. It has firstname, lastname, incomes, expenses properties and it has totalIncome, totalExpense, accountInfo,addIncome, addExpense and accountBalance methods. Incomes is a set of incomes and its description and expenses is also a set of expenses and its description.

const personAccount = {
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


const personJSON = JSON.stringify(personAccount)

localStorage.setItem("personAccount",personJSON)