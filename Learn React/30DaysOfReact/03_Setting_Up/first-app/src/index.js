import React from 'react'
import ReactDOM from 'react-dom/client'
import userImg from './user-img.jpg'
import './index.css'

const title = <h2>Getting started with React</h2>

const user = (
  <div >
    <img src={userImg} alt='author-image' width='100%'></img>
  </div>
)

// JSX element, header
const header = (
  <header className='header-wrapper'>
      {user}
      <h1>Welcome to 30 Days Of React</h1>
      {title}
      <h3>JavaScript Library</h3>
      <p>Asabeneh Yetayeh</p>
      <small>Oct 2, 2020</small>
    
  </header>
)

// JSX element, main

const main = (
  <main className = 'main-wrapper'>
    <p>Prerequisite to get started react.js:</p>
    <ul>
      <li>HTML</li>
      <li>CSS</li>
      <li>JavaScript</li>
    </ul>
  </main>
)


// JSX element, footer
const footer = (
  <footer className='footer-wrapper'>
    <p>Copyright 2020</p>
  </footer>
)

// JSX element, app, a container or a parent
const app = (
  <div>
    {header}
    {main}
    {footer}
  </div>
)





const rootEle = ReactDOM.createRoot(document.getElementById('root'))

rootEle.render(app)