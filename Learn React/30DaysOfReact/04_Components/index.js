// React can we written with functional and class based component

// Functional component => function that returns jsx

const jsx = <tag>Hello</tag>
const ComponentName = () => {
    return jsx
}

// JSX element, header
const header = (
    <header style={headerStyles}>
      <div className='header-wrapper'>
        <h1>Welcome to 30 Days Of React</h1>
        <h2>Getting Started React</h2>
        <h3>JavaScript Library</h3>
        <p>Asabeneh Yetayeh</p>
        <small>Oct 3, 2020</small>
      </div>
    </header>
  )

  
  
  // React Component
  const Header = () => {
    return header
  }
  
  // or we can just return the JSX
  
  const Header1 = () => {
    return (
      <header style={headerStyles}>
        <div className='header-wrapper'>
          <h1>Welcome to 30 Days Of React</h1>
          <h2>Getting Started React</h2>
          <h3>JavaScript Library</h3>
          <p>Asabeneh Yetayeh</p>
          <small>Oct 3, 2020</small>
        </div>
      </header>
    )
  }
  
  // Even th above code can be written like this
  // Explicitly returning the JSX
  const Header2 = () => (
    <header style={headerStyles}>
      <div className='header-wrapper'>
        <h1>Welcome to 30 Days Of React</h1>
        <h2>Getting Started React</h2>
        <h3>JavaScript Library</h3>
        <p>Asabeneh Yetayeh</p>
        <small>Oct 3, 2020</small>
      </div>
    </header>
  )