import React, { Component } from 'react';
import Guitar from './components/chords/guitar'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        ChordMe
      </header>
      <Guitar />
    </div>
  );
}

export default App;
