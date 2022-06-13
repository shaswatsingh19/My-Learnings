const btn = document.querySelector('button')
const appendBtn = document.querySelector('#append-btn')

btn.onclick = () => {
    // btn.innerHTML = '<li>sda</li>' does not insert text it see this as html and but a list item
    // btn.innerText = '<li>sda</li>'  goes as a text inside HTML of button 
    btn.innerText = 'HELLO'
    
}


const btn1 = document.querySelector('#my-button')
const btn2 = document.querySelector('#my-second-button')
const output = document.querySelector("#output")

btn1.onclick = () => {
output.innerText = btn1.innerText
}
btn2.onclick = () => {
output.innerText = btn2.innerHTML
}



appendBtn.onclick = () => {
    const h1 = document.createElement('h1')

    // document.body.appendChild(h1) // appendChild can only work with nodes, but append() function works with anything
    h1.innerText = "Appended by button using createElement function"

    // document.body.append('hello world ') // will append hello world after the button as normal text
    document.body.append(h1)

    btn1.prepend("prepending from append to document btn") // add the child to the top of the parent
    // can also accept multiple values


    setTimeout(() => {
        h1.remove()
    },3000)
}
