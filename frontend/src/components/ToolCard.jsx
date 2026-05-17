import React from 'react';

const ToolCard = ({ title, description }) => {
  return (
    <div className="bg-white rounded-lg shadow-lg p-6 m-4 w-64 text-center transform hover:scale-105 transition-transform duration-300">
      <h3 className="text-2xl font-formula text-accent-dark mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
};

export default ToolCard;
