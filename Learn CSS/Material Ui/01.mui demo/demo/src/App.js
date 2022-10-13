
import * as React from 'react';
import {Button , Typography , CssBaseline , Toolbar,AppBar, Container,Box } from '@mui/material';
import PhotoCameraIcon from '@mui/icons-material/PhotoCamera';

import {red } from '@mui/material/colors'

function App() {
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
        <div>
            <Container maxWidth='md'>
                <Typography variant='h2' align='center' color='primary'
                border={5} gutterBottom >
                    Photo Album 
                </Typography>
                <Typography paragraph align='center' color='secondary' gutterBottom >
                    Something short and leading about the collection below—its contents, the creator, etc. Make it short and sweet, but not too short so folks don't simply skip over it entirely. 
                </Typography>
                
            </Container>
        </div>
    </main>
    
  </>
  );
}


export default App;