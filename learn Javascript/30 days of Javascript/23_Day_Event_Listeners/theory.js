
const button = document.querySelector('button')

// button.addEventListener('click', e => {
//     console.log(e)
//     console.log(e.target)
//     console.log(e.target.textContent)
// })

// function onClick(){
//     alert('onclick() from HTML')
// }


document.body.addEventListener("click" , e => {
    console.log(e)
    console.log(e.target)
    console.log(e.target.textContent)
    
} , {once : true}) // with once function the event will only occur once

const eventArr = ["click - when the element clicked",
"dblclick - when the element double clicked",
"mouseenter - when the mouse point enter to the element",
"mouseleave - when the mouse pointer leave the element",
"mousemove - when the mouse pointer move on the element",
"mouseover - when the mouse pointer move on the element",
"mouseout -when the mouse pointer out from the element",
"input -when value enter to input field",
"change -when value change on input field",
"blur -when the element is not focused",
"keydown - when a key is down",
"keyup - when a key is up",
"keypress - when we press any key",
"onload - when the browser has finished loading a page"]
const ul = document.querySelector('ul')

for(let event of eventArr){
    const li = document.createElement('li')
    li.textContent = event
    li.style.listStyle = 'a'
    ul.append(li)

}


const input = document.querySelector('input')
      const p = document.querySelector('p')

      input.addEventListener('input', e => {
        p.textContent = e.target.value
      })
      
      document.querySelector('input').addEventListener('blur', (e) => {
        p.textContent = 'Field is required'
        p.style.color = 'red'

    })

