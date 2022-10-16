import React from "react";
import {  Stack } from "@mui/system";
import { logo } from "../utils/contants";
import { Link } from "react-router-dom";
import SearchBar from './SearchBar'


const Navbar = () => {
  return (
      <Stack 
        direction="row"
        alignItems="center"
        justifyContent='center'
        p={2}
        sx={{
          position:'sticky',
          top:'0',
          backgroundColor:'black',
          justifyContent:'space-between'
        }}
      >
        <Link to='/' style={{display:'flex', alignItems:'center', }}>
          <img src={logo} alt='logo' height={45}/>
        </Link>
        <SearchBar/>
      </Stack>
  );
};

export default Navbar;
