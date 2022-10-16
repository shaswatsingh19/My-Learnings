
import * as React from 'react';
import {Button , Typography , CssBaseline , Toolbar,AppBar, Container, Grid , Card, CardMedia, CardContent,CardActions} from '@mui/material';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';
import useStyles from './styles';
import img from './assets/img.jpg'

function App() {

    const card = [0,1,2,3,4,5,6,7]
    const classes = useStyles()
    
    return (
    <>
        <CssBaseline />
        <AppBar position='relative'>
            <Toolbar >
                <PhotoCameraIcon/>
                <Typography variant='h6' >
                    Photo Album
                </Typography>
            </Toolbar>
        </AppBar>

        <main>
            <div className={classes.container}>
                <Container maxWidth='md'>
                    <Typography variant='h2' align='center' color='primary' gutterBottom >
                        Photo Album 
                    </Typography>
                    <Typography paragraph align='center' color='secondary' gutterBottom >
                        Hello everyone, this is a photo album I am using to learn material UI and adding different photo using mui components.    
                    </Typography>
                    <div>
                        <Grid container spacing={2} justifyContent='center'>
                            <Grid item>
                                <Button variant='contained'>See my photos</Button>
                            </Grid>
                            <Grid item>
                                <Button variant='outlined' >Secondary Button</Button>
                            </Grid>
                        </Grid>
                    </div>
                </Container>
            </div>

            <Container className={classes.cardGrid}>
                <Grid container spacing={4}>

                    {card.map((c,i) => {
                        return (
                            <Grid item xs={12} sm={6} lg={4} key={i} >
                                <Card className={classes.card}>
                                <CardMedia 
                                    className={classes.cardMedia}
                                    image={img}
                                    height='10px'
                                    title='image title '    
                                />
                                
                                <CardContent className={classes.cardContent}>
                                    <Typography variant='h5' gutterBottom>
                                        Image of Lord Ganesha
                                    </Typography>
                                    <Typography variant='h6' gutterBottom>
                                        Ganesha, also known as Ganapati, Vinayaka, and Pillaiyar, is one of the best-known and most worshipped deities in the Hindu pantheon
                                    </Typography>
                                </CardContent>
                                <CardActions>
                                    <Button size='small'>View</Button>
                                    <Button size='small'>Edit</Button>
                                </CardActions>
                            </Card>
                    </Grid>
                        )
                    })}
                      
                </Grid>
            </Container>
        </main>

        <footer className={classes.footer}>
            <Typography variant='h6' gutterBottom >Thanks for visiting</Typography>
            <Typography variant='subtitle1'>Something here to give the footer a purpose!</Typography>
        </footer>
        
    </>
    );
}


export default App;