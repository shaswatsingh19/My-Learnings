console.log('LEVEL 1')

// Create an Animal class. The class will have name, age, color, legs properties and create different methods
class Animal {
    constructor (name,type,age,color,legs){
        this.name = name
        this.age = age
        this.color = color
        this.legs = legs
        this.sound =''
        this.type = type
    }

    set setSound(sound){
        this.sound = sound
    }

    get getSound(){
        return `${this.type} makes ${this.sound} sound`
    }

    walk(){
        return `A ${this.type} named ${this.name} is walking`
    }
}

// Create a Dog and Cat child class from the Animal Class.
const d1 = new Animal('tony','dog',3,"grey",4)
d1.setSound = 'bark'
console.log(d1.walk())
const c1 = new Animal('perry','cat',1,'white',4)
c1.setSound = 'Meow'
console.log(c1.getSound)


console.log("LEVEL 2")

// Override the method you create in Animal class
class Dog extends Animal{
    constructor(name,age,color,legs,type='dog'){
        super(name,type,age,color,legs)
    }

    walk(){
        if (this.legs<3){
            return `${this.name} can't walk`
        }
        
    }
}

const d2 = new Dog('radha',3,"pink",4)
console.log(d2.walk())



/*
Let's try to develop a program which calculate measure of central tendency of a sample(mean, median, mode) and measure of variability(range, variance, standard deviation). In addition to those measures find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions which do statistical calculations as method for the Statistics class. Check the output below.
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

console.log('Count:', statistics.count()) // 25
console.log('Sum: ', statistics.sum()) // 744
console.log('Min: ', statistics.min()) // 24
console.log('Max: ', statistics.max()) // 38
console.log('Range: ', statistics.range() // 14
console.log('Mean: ', statistics.mean()) // 30
console.log('Median: ',statistics.median()) // 29
console.log('Mode: ', statistics.mode()) // {'mode': 26, 'count': 5}
console.log('Variance: ',statistics.var()) // 17.5
console.log('Standard Deviation: ', statistics.std()) // 4.2
console.log('Variance: ',statistics.var()) // 17.5
console.log('Frequency Distribution: ',statistics.freqDist()) // [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
// you output should look like this
console.log(statistics.describe())
Count: 25
Sum:  744
Min:  24
Max:  38
Range:  14
Mean:  30
Median:  29
Mode:  (26, 5)
Variance:  17.5
Standard Deviation:  4.2
Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has totalIncome, totalExpense, accountInfo,addIncome, addExpense and accountBalance methods. Incomes is a set of incomes and its description and expenses is also a set of expenses and its description.
 */