class Emp {
    constructor(firstName,lastName,id,sal){
        this.firstName = firstName
        this.lastName = lastName
        this.sal =  sal
        this.id = id
        this.skills = []
    }

    getFullName(){
        const fullName = this.firstName +' '+this.lastName
        return fullName
    }
    get getSalary(){
        return this.sal
    }
    get getSkills(){
        return this.skills
    }
    set setSkills(skill){
        this.skills.push(skill)
    }


}

const emp1 = new Emp('Santosh','Sinha',1,22)
console.log(emp1.getFullName())
console.log(emp1.getSalary) //Not a function it is a property
emp1.setSkills = 'HTML'
emp1.setSkills = 'CSS'
emp1.setSkills = 'Python'
console.log(emp1.getSkills)


// Static method

class Test{

    constructor(){
        console.log(Test.display() +" called from constuctor")
        console.log(this.constructor.display()) // invoke static method with constructor
    }
    static display(){
        return ('In static method can be more than 1')
    }
    static display(){
        return ('2nd display method, js always envoke the last function if given same name')
    }
}

const obj = new Test()
// obj.constuctor(1)
console.log(Test.display()) // object can't call static method
// obj.display or obj.display gives error




// ENCAPSULATION
// Bind the data to function to avoid direct access to data members

class Student{
    constructor(){
        var name
        var age
    }

    /**
     * @param {string} name
     */
    set setName(name){
        this.name = name
    }
    /**
     * @param {number} age
     */
    set setAge(age){
        this.age = age
    }

    get getName(){
        return this.name
    }

    get getAge(){
        return this.age
    }

}

const std1 = new Student()
std1.setName = 'Ram'
std1.setAge = 14


console.log(std1.getName)
console.log(std1.getAge)
