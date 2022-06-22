document.body.style.textAlign = 'center'
document.body.style.background= ' linear-gradient(to right, #283048, #859398)'

const input = document.querySelector('input')
const select = document.querySelector('select')
const button = document.querySelector('button')
const image = document.getElementsByClassName('image')

const gravity = {
  'Earth' : 9.8,
  'Jupiter':	24.92,
  "Neptune":11.15,
  "Saturn":	10.44,
  "Uranus":	8.87,
  "Venus":8.87,
  "Mars":3.71,
  "Mercury":3.7,
  "Moon":1.62,
	"Pluto":0.58
}

input.addEventListener('input', (e) => {

  console.log(e.target.value)
  const massKG = e.target.value
  select.addEventListener("change",ev => {
    console.log(ev.target.value)
    var planet = ev.target.value

    image.append = "<img src='./images/earth.png' class='planet-image' />"
    
    button.addEventListener('click', btn => {
    console.log(gravity[planet]*massKG)
    })
  })

})