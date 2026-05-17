# iLovePDFPrivacy

A self-hosted, privacy-focused alternative to online PDF tools. Process files locally without uploading them to third-party servers.

## Features

- Merge multiple PDF files into one
- Split PDFs by page ranges
- Compress PDFs to reduce file size
- Convert Word documents to PDF
- Convert PowerPoint presentations to PDF
- Convert images into a single PDF

## Local Development

### Prerequisites

- Python 3.8+
- Node.js v18+
- npm

---

## Backend Setup

### 1. Navigate to the backend directory

```bash
cd backend
```

### 2. Create and activate a virtual environment

#### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the backend server

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

## Frontend Setup

### 1. Navigate to the frontend directory

```bash
cd frontend
```

### 2. Install dependencies

```bash
npm install
```

### 3. Start the development server

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

## Upcoming Features

- Docker support for one-command setup
- OCR support for scanned PDFs
- PDF encryption and password protection
- Batch processing support