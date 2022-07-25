const menu = document.querySelector('.nav-toggle')
const navList = document.querySelector('#nav-list')


menu.addEventListener('click',()=>{
    navList.classList.toggle('nav-visible')
})