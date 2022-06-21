

/*
Develop the following application, use the following HTML elements to get started with. You will get the same code on starter folder. Apply all the styles and functionality using JavaScript only.

The year color is changing every 1 second
The date and time background color is changing every on seconds
Completed challenge has background green
Ongoing challenge has background yellow
Coming challenges have background red
 */

document.body.style.textAlign = 'center'

const year = document.getElementById('year')
const h2 = document.querySelector('h2')
const timeNow  = document.getElementById('time-now')
const li  = document.querySelectorAll('li')


year.style.fontSize = '5rem'

timeNow.style.padding = '4px 15px'
timeNow.style.fontWeight = '900'
timeNow.style.fontSize = '1rem'


li.forEach( (list) => {
    list.style.listStyle = 'none'
    list.style.margin  = '2px'
    list.style.display = 'inline-block'
    list.style.width = '60%'
    list.style.fontSize = '1.5rem'
    list.style.padding = '12px 10px'
    if(list.textContent.includes('Done')){
        list.style.background = 'green'
    }else if (list.textContent.includes('Ongoing')){
        list.style.background = 'orange'
    }else {
        list.style.background = 'red'
    }
})




const randomColor = () => {
    const r = Math.floor(Math.random()*256)
    const g = Math.floor(Math.random()*256)
    const b = Math.floor(Math.random()*256)
    return `rgb(${r},${g},${b})` 
}


setInterval(() => {    
    year.style.color = randomColor()
    timeNow.style.background = randomColor()
    const now = new Date()
    timeNow.textContent = now.toString().substring(0,24)      
    
    
    
},1000)

