console.log('Creating Element')

const h3 = document.createElement('h3')

h3.textContent = 'Day 22 Exercise'
h3.style.fontSize = '24px'
console.log(h3)

document.body.append(h3)

const h4 = document.createElement('h4')


document.body.append(h4)

var i =5

setInterval(() =>{
    h4.textContent = 'Will be removed in '+i+'sec'
    h4.style.fontSize = '24px'
    i-=1
},1000)

setTimeout(() => {
    document.body.removeChild(h4)
},6100)

