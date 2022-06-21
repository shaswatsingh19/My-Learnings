

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


// li.forEach( (list) => {
//     list.style.listStyle = 'none'
//     list.style.margin  = '2px'
//     list.style.display = 'inline-block'
//     list.style.width = '60%'
//     list.style.fontSize = '1.5rem'
//     list.style.padding = '12px 10px'
//     if(list.textContent.includes('Done')){
//         list.style.background = 'green'
//     }else if (list.textContent.includes('Ongoing')){
//         list.style.background = 'orange'
//     }else {
//         list.style.background = 'red'
//     }
// })

const ul = document.querySelector('ul')
console.log(ul)
ul.style.padding = '5px'

for(let challenge of challenge2022.challenges){
    const list = document.createElement('li')
    list.style.display = 'grid'
    list.style.gridTemplateColumns = 'repeat(3,1fr)'
    list.style.margin = '5px'
    list.style.padding = '20px 15px'

    const challengeName = document.createElement('span')
    challengeName.textContent = challenge.name
    challengeName.style.textDecoration = 'underline'

    const challengeDetails = document.createElement('span')
    let topicArray = ''
    for(let i=1;i<challenge.topics.length;i++){
        const topic = challenge.topics[i]
        console.log(topic)
        topicArray += '<div>'+topic+'</div>'

    }
    
    challengeDetails.innerHTML = "<details><summary>"+challenge.topics[0]+"</summary><div>"+topicArray+"</div></details>"
    // challengeDetails.style.display = 'grid'
    

    const challengeStatus = document.createElement('span')
    challengeStatus.textContent = challenge.status

    list.append(challengeName,challengeDetails,challengeStatus)
    ul.appendChild(list)

    console.log(list.textContent.includes('Done'))


    if(list.textContent.includes('Done')){
        list.style.background = 'green'
    }else if (list.textContent.includes('Ongoing')){
        list.style.background = 'orange'
    }else {
        list.style.background = 'red'
    }

}




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

