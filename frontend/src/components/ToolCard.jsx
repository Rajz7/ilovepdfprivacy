import React from 'react';
import { Link } from 'react-router-dom';

const ToolCard = ({ title, description, path }) => {
  return (
    <Link
      to={path}
      className="block bg-white rounded-lg shadow-lg p-6 m-4 w-64 text-center transform hover:scale-105 transition-transform duration-300"
    >
      <h3 className="text-2xl font-formula text-accent-dark mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </Link>
  );
};

export default ToolCard;
