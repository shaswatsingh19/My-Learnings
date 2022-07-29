import React from 'react'
import ReactDOM from 'react-dom/client'
import myImg from './images/my-img.jpg'

let userName = 'Shaswat Singh'
let role = 'FrontEnd Developer'
let location  = "India"
let skills = ['HTML','CSS','Javascript','React','MySQL','Git','Python']
let skillsList = skills.map( (skill) => <li key={skill} className='list-item'>{skill}</li>)
let date = 'July 29, 2022'

const header = (
    <header>
        <div className='header-wrapper'>
            <img src={myImg} alt='user-img'></img>
            <h1>
                {userName}
            </h1>
            <h2>
                {role},  {location}
            </h2>
            <h3>Skills</h3>
            <ul className='skill-list'> 
                {skillsList}
                
            </ul>
            <small>{date}</small>
        </div>
    </header>
)

const appStyle = {background:'white', padding:"20px"}
const app = (
    <div style={appStyle}>
        {header}
    </div>
)

const rootEle = ReactDOM.createRoot(document.getElementById('root'))
rootEle.render(app)
