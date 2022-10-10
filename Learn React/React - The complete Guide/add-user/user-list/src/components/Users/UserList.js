import Card from "../UI/Card"
import classes from './UserList.module.css'

export default function UserList(props){
    
    return (
        <Card className={classes.users}>
            <ul>
                {
                    props.users.map((user) => {
                    return <li key={user.id} >{user.name} is {user.age} years old</li>
                    })
                }
            </ul>
        </Card>

    )

}