import React from 'react';
import ReactDOM from 'react-dom/client';
import deadpool from './images/deadpool.jpg'
import ironMan from './images/iron-man.jpg'
import moonknight from './images/moonknight.jpg'
import { header } from './components/header';

const main = (
  <main>
    <div class='main-wrapper'>
      <img src={deadpool} alt='deadpool'></img>
      <img src={ironMan} alt='iron-man'></img>
      <img src={moonknight} alt='moonknight'></img>
    </div>
  </main>
)


const app = (
  <div id='app-container'>
    {header}
    {main}
  </div>
)

const rootEle = ReactDOM.createRoot(document.getElementById('root'))

rootEle.render(app)