console.log('LEVEL 1')

// Create an index.html file and put four p elements as above: Get the first paragraph by using document.querySelector(tagname) and tag name

const firstPara = document.querySelector('p')
console.log(firstPara)

// Get each of the the paragraph using document.querySelector('#id') and by their id

const lastPara = document.querySelector('#p4')
console.log(lastPara)

// Get all the p as nodeList using document.querySelectorAll(tagname) and by their tag name
const allP = document.querySelectorAll('p')
console.log(allP)

// Loop through the nodeList and get the text content of each paragraph
allP.forEach( (para) => console.log(para.textContent))

// Set a text content to paragraph the fourth paragraph,Fourth Paragraph
allP[3].textContent = 'Fourth Paragraph'

// Set id and class attribute for all the paragraphs using different attribute setting methods

allP[0].id = 'para 1 id'
allP[1].setAttribute('class','para 2 class')
allP[2].classList.add('para_3','para_3_class')
// allP[2].classList.add('para 3','para 3 class') can't have space as we are adding multiple classes


console.log('LEVEL 2')

// Change stye of each paragraph using JavaScript(eg. color, background, border, font-size, font-family)
allP[0].style.fontSize = '2rem'
allP[1].style.background = 'red'
allP[2].style.border = '3px dashed grey'
allP[2].style.background = 'linear-gradient(to right, #a91711, #f5af19)'
allP[2].style.fontWeight = 'bolder'
allP[2].style.padding = "5px"
allP[2].style.textAlign = 'center'
allP[3].style.textDecoration = 'underline'

console.log('LEVEL 3')
