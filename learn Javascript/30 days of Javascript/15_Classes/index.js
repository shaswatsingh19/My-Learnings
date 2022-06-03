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


