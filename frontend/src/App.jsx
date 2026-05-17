import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ToolPage from './pages/ToolPage';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/tool/:toolName" element={<ToolPage />} />
      </Routes>
    </Router>
  );
};

export default App;
