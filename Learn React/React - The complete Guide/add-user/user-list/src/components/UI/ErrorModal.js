import Card from './Card'
import Button from './Button'
import classes from './ErrorModal.module.css'

export default function ErrorModal(props){
    
    return (
        <div  onClick={props.onClick} className = {classes.backdrop}>
        <Card className={classes.modal}>
            <header className={classes.header}>
                <h2>{props.title}</h2>
            </header>
            <div className={classes.content}>
                <p>{props.message}</p>
            </div>
            <footer className={classes.actions}>
                <Button onClick={props.onClick}>Close Me</Button>
            </footer>
        </Card>
        </div>
    )
}