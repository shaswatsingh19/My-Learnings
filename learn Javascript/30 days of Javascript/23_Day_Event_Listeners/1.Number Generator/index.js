console.log('LEVEL 1')

document.body.style.textAlign = 'center'
document.body.margin = 0
document.body.padding = 0

const input = document.getElementById('input')
const container = document.querySelector('div')
const generateBtn = document.querySelector('button')
const error = document.getElementById('error')

container.style.margin = '20px 50px'
container.style.display = 'grid'
container.style.gridTemplateColumns = 'repeat(10,1fr)'

input.addEventListener('input' , e => {
    // console.log(e.target.value)
    let range  = e.target.value 

    generateBtn.addEventListener('click', function (){
        container.textContent = ''
        error.textContent = ''       
        if (range/1){
            generateNum(range)

        }else{
            error.textContent = 'input value should be a number'
            error.style.color = 'red'
        }
    })
})

const  generateNum = function (range) {
    for(let i = 0;i<=range;i++){
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
}

function isPrime(num){
    for(let i=2;i*i<=num;i++){
        if (num%i == 0){
            return false
        }
    }
    return true

}