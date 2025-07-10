import React, { useState } from 'react';

function Greeting(props) {
  const [message, setMessage] = useState("Welcome to React!");

  return (
    <div>
      <h2>{message}</h2>
      <p>Hello, {props.name}!</p>
      <button onClick={() => setMessage("Thanks for visiting!")}>
        Click Me
      </button>
    </div>
  );
}

export default Greeting;
