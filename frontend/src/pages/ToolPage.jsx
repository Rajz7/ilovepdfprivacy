import React, { useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { mergePdf, splitPdf, compressPdf, imageToPdf, wordToPdf, pptToPdf } from '../api/pdf';

const TOOL_DEFAULT_FILENAMES = {
  'merge-pdf': 'merged.pdf',
  'split-pdf': 'split_files.zip',
  'compress-pdf': 'compressed.pdf',
  'image-to-pdf': 'converted.pdf',
  'word-to-pdf': 'converted.pdf',
  'powerpoint-to-pdf': 'converted.pdf',
};

const CONTENT_TYPE_EXTENSIONS = {
  'application/pdf': '.pdf',
  'application/zip': '.zip',
};

const getFilenameFromContentDisposition = (contentDisposition) => {
  if (!contentDisposition) {
    return null;
  }

  const utf8Match = contentDisposition.match(/filename\*=UTF-8''([^;]+)/i);
  if (utf8Match?.[1]) {
    return decodeURIComponent(utf8Match[1].trim().replace(/"/g, ''));
  }

  const basicMatch = contentDisposition.match(/filename=([^;]+)/i);
  if (basicMatch?.[1]) {
    return basicMatch[1].trim().replace(/^"|"$/g, '');
  }

  return null;
};

const ensureFilenameExtension = (filename, contentType) => {
  const extension = CONTENT_TYPE_EXTENSIONS[contentType];
  if (!extension) {
    return filename;
  }

  if (filename.toLowerCase().endsWith(extension)) {
    return filename;
  }

  return `${filename}${extension}`;
};

const ToolPage = () => {
  const { toolName } = useParams();
  const [files, setFiles] = useState([]);
  const [ranges, setRanges] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    setFiles([...e.target.files]);
    setError(null);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setError(null);
    try {
      let response;
      switch (toolName) {
        case 'merge-pdf':
          response = await mergePdf(files);
          break;
        case 'split-pdf':
          response = await splitPdf(files[0], ranges);
          break;
        case 'compress-pdf':
          response = await compressPdf(files[0]);
          break;
        case 'image-to-pdf':
          response = await imageToPdf(files);
          break;
        case 'word-to-pdf':
          response = await wordToPdf(files[0]);
          break;
        case 'powerpoint-to-pdf':
          response = await pptToPdf(files[0]);
          break;
        default:
          throw new Error('Invalid tool');
      }

      const blob = response.data;
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      const contentDisposition = response.headers['content-disposition'];
      const contentType = response.headers['content-type'];
      const fallbackFilename = TOOL_DEFAULT_FILENAMES[toolName] || 'download';
      const extractedFilename = getFilenameFromContentDisposition(contentDisposition);
      const filename = ensureFilenameExtension(extractedFilename || fallbackFilename, contentType);
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
      setFiles([]);
      setRanges('');

    } catch (err) {
      console.error('Error processing files:', err);
      const errorMessage = err.response?.data?.detail || 'An error occurred. Please try again.';
      setError(errorMessage);
    } finally {
      setIsLoading(false);
    }
  };

  const title = toolName.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
  const isMultiFile = toolName === 'merge-pdf' || toolName === 'image-to-pdf';

  return (
    <div className="min-h-screen flex flex-col items-center justify-center p-4 bg-gray-50">
       <div className="absolute top-4 left-4">
            <Link to="/" className="text-accent-dark hover:text-accent-pink font-bold py-2 px-4 rounded">
                &larr; Back to Home
            </Link>
        </div>
      <div className="w-full max-w-2xl p-8 space-y-8 bg-white rounded-2xl shadow-lg">
        <h1 className="text-4xl font-formula text-accent-dark text-center">{title}</h1>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="flex flex-col items-center justify-center w-full">
            <label htmlFor="file-upload" className="flex flex-col items-center justify-center w-full h-64 border-2 border-accent-pink border-dashed rounded-lg cursor-pointer bg-gray-50 hover:bg-gray-100">
              <div className="flex flex-col items-center justify-center pt-5 pb-6">
                <svg className="w-10 h-10 mb-3 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16a4 4 0 01-4-4V7a4 4 0 014-4h1.586a1 1 0 01.707.293l1.414 1.414a1 1 0 00.707.293H13a4 4 0 014 4v1.586a1 1 0 01-.293.707l-1.414 1.414a1 1 0 00-.293.707V16m-7-2h2m-2 4h2"></path></svg>
                <p className="mb-2 text-sm text-gray-500"><span className="font-semibold">Click to upload</span> or drag and drop</p>
                <p className="text-xs text-gray-500">{isMultiFile ? 'Upload multiple files' : 'Upload a single file'}</p>
              </div>
              <input id="file-upload" type="file" multiple={isMultiFile} onChange={handleFileChange} className="hidden" />
            </label>
            <div className="mt-4 w-full text-center">
              {files.map((file, index) => (
                <p key={index} className="text-sm text-gray-600 truncate">{file.name}</p>
              ))}
            </div>
          </div>

          {toolName === 'split-pdf' && (
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="ranges">
                Page Ranges (e.g., 1-3,5,7-9)
              </label>
              <input
                type="text"
                id="ranges"
                value={ranges}
                onChange={(e) => setRanges(e.target.value)}
                className="shadow-sm appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:ring-2 focus:ring-accent-pink focus:border-transparent"
                required
              />
            </div>
          )}

          {error && (
            <div className="p-4 text-sm text-red-700 bg-red-100 rounded-lg" role="alert">
              <span className="font-medium">Error:</span> {error}
            </div>
          )}

          <div className="flex items-center justify-center">
            <button
              type="submit"
              disabled={isLoading || files.length === 0}
              className="w-full bg-accent-pink hover:bg-pink-400 text-accent-dark font-bold py-3 px-4 rounded-lg focus:outline-none focus:shadow-outline disabled:bg-gray-400 transition-colors duration-300"
            >
              {isLoading ? 'Processing...' : 'Process Files'}
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ToolPage;