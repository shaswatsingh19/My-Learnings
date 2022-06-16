console.log('LEVEL 1')

/*
Create a div container on HTML document and create 100 to 100 numbers dynamically and append to the container div.
Even numbers background is green
Odd numbers background is yellow
Prime numbers background is red
*/

let container = document.getElementById('container')
container.style.margin = '10px 50px'
container.style.display = 'grid'
container.style.gridTemplateColumns = 'repeat(6,1fr)'

for(let i = 0;i<=100;i++){
    const span = document.createElement('span')
    span.textContent = i
    span.style.margin = '1px'
    span.style.padding = '15px 15px'
    span.style.textAlign = 'center'
    span.style.fontSize = '1.5rem'    
    container.append(span)

    if (i==0) span.style.background = '#21bf73'
    if (i==1) span.style.background = '#fddb3a'

    else if (isPrime(i)){
        span.style.background = '#fd5e53'
    }
    else if (i%2 == 0){
        span.style.background = '#21bf73'
    }
    else{
        span.style.background = '#fddb3a'
    }
}

function isPrime(num){
    for(let i=2;i*i<=num;i++){
        if (num%i == 0){
            return false
        }
    }
    return true

}


/*
Use the countries array to display all the countries.See the design
 */
container = document.getElementById('countries-container')


let countryHeading = document.createElement('h1')
countryHeading.textContent = 'WORLD COUNTRIES LIST'
container.appendChild(countryHeading)
container.style.textAlign = 'center'
container.style.margin = '10px 50px'

let countriesLength = document.createElement('h3')
countriesLength.textContent = "Total number of countries: "+countriesArray.length
container.appendChild(countriesLength)

let countriesList = document.createElement('div')
container.append(countriesList)
countriesList.style.display = 'grid'
countriesList.style.gridTemplateColumns = 'repeat(5,1fr)'

for(let country of countriesArray){
    const countryName = document.createElement('span')
    countryName.textContent = country.name
    countryName.style.textAlign = 'center'
    countryName.style.padding = '40px 5px'
    countryName.style.margin = '2px'
    countryName.style.border = '2px solid grey'
    countryName.style.borderRadius = '2px'
    countryName.style.boxShadow = '0px 0px 2px #f8f8f1'
    countryName.style.textTransform = 'uppercase'
    countryName.style.fontWeight = '900'
    countryName.style.color = "#4f4f4f"
    countriesList.appendChild(countryName)
}


console.log('LEVEL 3')
/*
Check the requirement of this project from both images(jpg and gif). All the data and CSS has been implemented using JavaScript only. The data is found on starter folder project_3. The drop down button has been created using details HTML element.

This challenges is in DOM MINI PROJECT FOLDER
 */
