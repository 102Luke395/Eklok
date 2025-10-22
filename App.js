import './App.css';
import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import Userlist from './Dashboard/Userslist'
import React from 'react';

function App() {
  return(
    <Router>
      <Routes>
      <Route path='/' element={<Userlist />}/>
      </Routes>
    </Router>
  );
}

export default App;
