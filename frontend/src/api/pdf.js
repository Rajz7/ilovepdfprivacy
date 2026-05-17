import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000', // Adjust this to your backend URL
  headers: {
    'Content-Type': 'multipart/form-data',
  },
});

export const mergePdf = (files) => {
  const formData = new FormData();
  files.forEach(file => {
    formData.append('files', file);
  });
  return apiClient.post('/pdf/merge-pdf/', formData, {
    responseType: 'blob',
  });
};

export const splitPdf = (file, ranges) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('ranges', ranges);
  return apiClient.post('/pdf/split-pdf/', formData, {
    responseType: 'blob',
  });
};

export const compressPdf = (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/pdf/compress-pdf/', formData, {
      responseType: 'blob',
    });
  };

export const imageToPdf = (files) => {
    const formData = new FormData();
    files.forEach(file => {
        formData.append('files', file);
    });
    return apiClient.post('/convert/images-to-pdf/', formData, {
        responseType: 'blob',
    });
};

export const wordToPdf = (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/convert/word-to-pdf/', formData, {
        responseType: 'blob',
    });
};

export const pptToPdf = (file) => {
    const formData = new FormData();
    formData.append('file', file);
    return apiClient.post('/convert/ppt-to-pdf/', formData, {
        responseType: 'blob',
    });
};
