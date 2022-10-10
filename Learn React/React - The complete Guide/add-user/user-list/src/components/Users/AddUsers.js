import React from 'react'
import Card from '../UI/Card'
import Button from '../UI/Button'

import classes from './AddUsers.module.css'



export default function AddUsers(props){
    
    const [formData , setFormData] = React.useState({
        'username' : '',
        'age' : ''
    })
    
    function submitHandler(event){
        event.preventDefault();
        
        if(formData.username.trim() === 0 || formData.age.trim === 0){
            return
        }
        // adding a + before converts it to a interger
        if(+formData.age < 1){
            return
        }
        console.log(formData)
        props.onAddUser(formData.username,formData.age)

        setFormData({
            'username':"",
            'age':""
        })
    }

    function changeHandler(event){
        const {name,value } = event.target

        setFormData((prevState) => {
            
            return {
                ...prevState,
                [name] : value}
        })
    }
    
    return (
        <Card className={classes.input}>
            <form onSubmit={submitHandler} >
                <label htmlFor='username'>User Name:</label>
                <input type='text' id='username' name='username' value={formData.username} onChange={changeHandler}/>
                <label htmlFor='age'>Age (in Years):</label>
                <input type='number' id='age' name='age' value={formData.age} onChange={changeHandler} />
                <Button type='submit'>ADD Users</Button>
            </form>
            
        </Card>
    )
}


