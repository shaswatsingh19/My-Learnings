/*
function fun1 (){
    return new Promise((resolve,reject) => {
        setTimeout(() => {
            if (0){
                console.log('Promise Resolved')
                resolve()
            }
            else{
                reject('Sorry doesn\'t runs') // default value to check else if given in catch block thing will run

            }
        }, 1000)
    })
}

fun1().then(function(){
    console.log('Resolved function') // goes to resolve() return value
}).catch(function(){
    console.log('Unresolved Function')
})


const doPromise = new Promise((resolve,reject) => {
    setTimeout(() => {
        const skills = ["HTML","CSS","JS"]
        if (skills.includes('React')){
            resolve('FRONTEND DEV')
        }
        else{
            reject('DEV')
        }

    } , 3000)
})

doPromise
.then((result)=>{
    console.log(result)
})
.catch((error) => {
    console.log(error)
})
const url = 'https://restcountries.com/v2/all' // countries api

fetch(url)
  .then(response => response.json()) // accessing the API data as JSON
  .then(data => {console.log(data)}) // getting the data
  .catch(error => console.error(error)) // handling error if something wrong happens



const fetchData = async () => {
    try {
        const response = await fetch(url)
        console.log(response)
        const countries = await response.json()
        console.log(countries)
    }
    catch (err){
        
        console.log(err)
    }
}

fetchData()

*/