document.body.style.margin = "0"
document.body.style.padding = "0"
document.body.style.textAlign = 'center'
document.body.style.display = 'flex'
document.body.style.flexDirection = 'column'



const container = document.createElement('div')
const keyCode = document.createElement('div')


container.style.background = '#ffa'
container.style.boxShadow = '1px 1px 5px grey'
container.style.margin = '20px 40px'
container.style.padding = '20px'
container.style.fontSize = '2rem'


keyCode.style.background = 'grey'
keyCode.style.boxShadow = '1px 1px 5px grey'
keyCode.style.padding = '20px'
keyCode.style.margin = '20px 40px'
keyCode.style.fontSize = '2rem'



container.textContent = 'Press Any KeyBoard Key'
document.body.append(container)

document.body.addEventListener('keypress',e => {
    console.log(e)
    
    container.textContent = 'You read '+ e.key
    // document.querySelector('e.key').style.color = 'red'
    const key = e.keyCode
    keyCode.textContent = key
    document.body.append(keyCode)

})