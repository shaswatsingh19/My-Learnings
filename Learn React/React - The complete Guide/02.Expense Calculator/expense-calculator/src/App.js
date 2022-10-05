import ExpenseItem from './components/ExpenseItem'
import {ExpenseDate}  from './ExpenseDate'

const App = () => {
    
    const expenseComponent = ExpenseDate.map(expense => {
        return (
            <ExpenseItem  
                key= {expense.id}
                date={expense.date} 
                price={expense.price} 
                item= {expense.item}  
            />

        )
    })
    return (
        <>
        <h1>Let's Start</h1>
        {expenseComponent}        
        </>
    )
}

export default App ;


