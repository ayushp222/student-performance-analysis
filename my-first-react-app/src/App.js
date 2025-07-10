import React from 'react';
import './App.css';
import Greeting from './components/Greeting';

function App() {
  return (
    <div className="App">
      <h1>My First React App</h1>
      <Greeting name="Ayush" />
    </div>
  );
}

export default App;
