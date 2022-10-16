import {useState} from 'react'
import { useNavigation } from 'react-router-dom'

import { Paper,IconButton ,TextField} from '@mui/material'
import {Search} from '@mui/icons-material';

const SearchBar = () => {
  return (
    <Paper
        component='form'
        onSubmit={() => {}}
        sx={{ 
            pl:2,
            borderRadius:20,
            boxShadow:'none',
            mr :{sm:4}
        }}
    >   
        <input 
            className='search-bar'
            placeholder='search...'
            value = ''
            onChange={() => {}}            
        />
        <IconButton type='submit' sx={{ p:'10px' , color:'red'}}>
            <Search />
        </IconButton>
    </Paper>
  )
}

export default SearchBar