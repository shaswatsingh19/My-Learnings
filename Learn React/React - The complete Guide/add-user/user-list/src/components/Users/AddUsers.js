import React from 'react'
import Card from '../UI/Card'
import Button from '../UI/Button'

import classes from './AddUsers.module.css'
import ErrorModal from '../UI/ErrorModal'



export default function AddUsers(props){
    
    const [formData , setFormData] = React.useState({
        'username' : '',
        'age' : ''
    })
    const [error , setError ] = React.useState()
    
    function submitHandler(event){
        event.preventDefault();
        
        if(formData.username.trim().length === 0 || formData.age.trim().length === 0){
            console.log(formData)
            setError({
                'title':'Invalid Input',
                'message':'Please Enter Valid name or age(in years)'
            })
            return
        }
        // adding a + before converts it to a interger
        if(+formData.age < 1){
            setError({
                'title':'Invalid Age',
                'message':'Please Enter age( > 0)'
            })
            return                   
            
        }
        
        props.onAddUser(formData.username,formData.age)

        setFormData((prevState) => {
            return {
                ...prevState,
                'username':"",
                'age':""
            }
        })
        
    }

    function changeHandler(event){
        const {name,value } = event.target

        console.log(name,value)
        setFormData((prevState) => {
            return {
                ...prevState,
                [name] : value
            }
        })
    }

    function errorHandler(){
        setFormData(null)
    }
    
    return (
        <div>
        {error && (<ErrorModal title={error.title} message={error.message} onClick={errorHandler}/>)}
        <Card className={classes.input}>
            <form onSubmit={submitHandler} >
                <label htmlFor='username'>User Name:</label>
                <input type='text' id='username' name='username' value={formData.username} onChange={changeHandler}/>
                <label htmlFor='age'>Age (in Years):</label>
                <input type='number' id='age' name='age' value={formData.age} onChange={changeHandler} />
                <Button type='submit'>ADD Users</Button>
            </form>
        </Card>
        </div>
    )
}


