import './ExpenseItem.css'
import ExpenseDate from './ExpenseDate'
import React from 'react'

export default function ExpenseItem(props){

    const [title , setTitle ] = React.useState(props.item)


    function handleClick(){
        setTitle('NO TIME')
    }

    return (
        <div className="expense-item">
            <ExpenseDate date={props.date}/>
            <div className="expense-item__description">
                <h2>{title}</h2>
                <div className="expense-item__price">${props.price}</div>
            </div>
            <button onClick={handleClick}>d</button>
        </div>
    )
}