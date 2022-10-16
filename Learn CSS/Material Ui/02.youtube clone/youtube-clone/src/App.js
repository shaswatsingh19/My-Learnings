import {BrowserRouter, Route, Routes  } from 'react-router-dom'
import { Box } from '@mui/material'

import {Navbar , Feed, VideoDetail, ChannelDetail, SearchFeed } from './components/index'

const App = () => (
    <BrowserRouter >
        <Box sx={{backgroundColor:'pink'}}>
            <Navbar/>
            <Routes>
                <Route path='/' exact element = {<Feed/>} />
                <Route path='/video/:id' exact element = {<VideoDetail/>} />
                <Route path='/channel/:id' exact element = {<ChannelDetail/>} />
                <Route path='/search/:searchTerm' exact element = {<SearchFeed/>} />
            </Routes>
        </Box>
    </BrowserRouter>
)


export default App;