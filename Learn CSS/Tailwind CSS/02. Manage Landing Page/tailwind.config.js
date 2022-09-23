/** @type {import('tailwindcss').Config} */
module.exports = {
  // look for any  html file in root 
  content: ['./*.html'],
  theme: {
    // can add custom properties
    screens:{
      sm:"480px",
      md:"768px",
      lg:"976px",
      xl:"1440px",
    },
    extend: {
      colors:{
        
      }
    },
  },
  plugins: [],
}
