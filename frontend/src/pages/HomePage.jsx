import React from 'react';
import ToolCard from '../components/ToolCard';

const HomePage = () => {
  const tools = [
    { title: 'Merge PDF', description: 'Combine multiple PDFs into one.' },
    { title: 'Split PDF', description: 'Extract pages from a PDF.' },
    { title: 'Compress PDF', description: 'Reduce the file size of your PDF.' },
    { title: 'Word to PDF', description: 'Convert Word documents to PDF.' },
    { title: 'Powerpoint to PDF', description: 'Convert Powerpoint presentations to PDF.' },
    { title: 'Image to PDF', description: 'Convert images to PDF.' },
  ];

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4">
      <header className="text-center mb-12">
        <h1 className="text-7xl font-formula text-accent-dark">iLovePDFPrivacy</h1>
        <p className="text-2xl text-gray-700 mt-2">Your privacy-focused PDF toolkit.</p>
        <p className="text-md text-gray-500 mt-4">
          Process your files locally. No uploads, no tracking, just pure privacy.
        </p>
      </header>
      <main className="flex flex-wrap justify-center">
        {tools.map((tool) => (
          <ToolCard key={tool.title} title={tool.title} description={tool.description} />
        ))}
      </main>
      <footer className="text-center mt-12">
        <p className="text-gray-500">
          Made with ❤️ for your privacy.
        </p>
      </footer>
    </div>
  );
};

export default HomePage;
