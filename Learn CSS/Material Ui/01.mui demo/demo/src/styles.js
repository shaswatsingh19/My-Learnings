import { makeStyles } from '@mui/styles';

const useStyles = makeStyles((theme) => ({

    container :{
        
        margin:'20px auto',
        maxWidth:'90%',
    },
    cardGrid:{
        maxWidth:'md',
        padding:'20px 0'
    },
    card:{
        height:'100%',
        display:'flex',
        flexDirection:'column',
    
    },
    cardMedia:{
        
        padding:'56.25%'
    },
    cardContent:{
        flexGrow:1,
    },
    footer:{
        margin:'20px auto',
        textAlign:'center'
    }
}))
export default useStyles