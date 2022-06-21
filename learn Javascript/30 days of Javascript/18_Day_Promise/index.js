console.log('LEVEL 1')

const countriesAPI = 'https://restcountries.com/v2/all'
const catsAPI = 'https://api.thecatapi.com/v1/breeds'

// Read the countries API using fetch and print the name of country, capital, languages, population and area.

fetch(countriesAPI)
.then(response => response.json())
.then( data => {
    console.log(data[0])
    let  i =0
    // while (i < data.length){
    //     const country = data[i].name
    //     const capital = data[i].capital
    //     const languages = data[i].languages
    //     const population = data[i].population
    //     console.log(country)
    //     console.log(capital)
    //     console.log(languages)
    //     console.log(population)
    //     i+=1
    // }
    data.forEach( (country) => {
        console.log(`country:${country.name} capital:${country.capital} languages:${country.languages} population${country.population}`)
    })
} )
.catch(err => console.log(err))

// Exercises: Level 2
// Print out all the cat names in to catNames variable.
// Exercises: Level 3
// Read the cats api and find the average weight of cat in metric unit.
// Read the countries api and find out the 10 largest countries
// Read the countries api and count total number of languages in the world used as officials.
