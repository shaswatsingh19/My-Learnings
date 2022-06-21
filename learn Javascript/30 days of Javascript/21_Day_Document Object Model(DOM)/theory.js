// const btn = document.querySelector('button')
// const appendBtn = document.querySelector('#append-btn')
// const h1 = document.querySelector('h1')

// document.body.style.background = '#e55d87  linear-gradient(to right, #e55d87, #5fc3e4)'
// // background: -webkit-linear-gradient(to right, #F8CDDA, #1D2B64);  /* Chrome 10-25, Safari 5.1-6 */
// // background: linear-gradient(to right, #F8CDDA, #1D2B64); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */

// console.log('GETTING ELEMENT')

// console.log("1.BY TAGNAME")
// const allBtn = document.getElementsByTagName('button')

// console.log('adding attributes using className to all button')
// setTimeout(() => {
//     alert('cl1,cl2,cl3 will be removed in 5 sec ')
// },1000)

// for (let button of allBtn){
//     console.log(button) // accessed as an index
//     // button.className = 'designer-btn'
//     button.setAttribute('class','designer-btn')

//     button.classList.add('cl1','cl2','cl3')
    

//     setTimeout(() => {
//         button.classList.remove('cl1','cl2','cl3')
//     },6000)
// }


// h1.style.color = "#360940"
// h1.style.textAlign = 'center'





// btn.onclick = () => {
//     // btn.innerHTML = '<li>sda</li>' does not insert text it see this as html and but a list item
//     // btn.innerText = '<li>sda</li>'  goes as a text inside HTML of button 
//     // btn.textContent = 'HELLO'
//     btn.innerText = 'HELLOW'
    
    
// }


// const btn1 = document.querySelector('#my-button')
// const btn2 = document.querySelector('#my-second-button')
// const output = document.querySelector("#output")

// btn1.onclick = () => {
// output.innerText = btn1.innerText
// }
// btn2.onclick = () => {
// output.innerText = btn2.innerHTML
// }



// appendBtn.onclick = () => {
//     const h1 = document.createElement('h1')

//     // document.body.appendChild(h1) // appendChild can only work with nodes, but append() function works with anything
//     h1.innerText = "Appended by button using createElement function"

//     // document.body.append('hello world ') // will append hello world after the button as normal text
//     document.body.append(h1)

//     btn1.prepend("prepending from append to document btn") // add the child to the top of the parent
//     // can also accept multiple values


//     setTimeout(() => {
//         h1.remove()
//     },3000)
// }
