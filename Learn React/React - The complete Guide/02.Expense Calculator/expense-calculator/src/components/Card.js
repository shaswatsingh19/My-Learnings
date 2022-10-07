import { ExpenseData } from "../ExpenseData"
import ExpenseItem from "./ExpenseItem"

const expenseComponent = ExpenseData.map(expense => {
    return (
        <ExpenseItem  
            key= {expense.id}
            date={expense.date} 
            price={expense.price} 
            item= {expense.item}  
        />

    )
})



export {expenseComponent}