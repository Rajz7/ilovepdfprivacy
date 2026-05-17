from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
from app.services.pdf.split_service import split_pdf
import os
import tempfile
import logging

router = APIRouter()

@router.post("/split-pdf/")
async def split_pdf_endpoint(file: UploadFile = File(...), ranges: str = Form(...)):
    """Endpoint to split a PDF file based on page ranges."""
    try:
        # Create a temporary file to store the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input_file:
            temp_input_file.write(await file.read())
            input_path = temp_input_file.name

        output_dir = tempfile.gettempdir()
        zip_path = split_pdf(input_path, ranges, output_dir)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            # Clean up the files after sending the response
            os.remove(file_path)
            os.remove(input_path)

        return StreamingResponse(
            file_iterator(zip_path),
            media_type="application/zip",
            headers={"Content-Disposition": f"attachment; filename=split_files.zip"}
        )

    except ValueError as e:
        logging.error(f"Invalid page range provided: {e}")
        os.remove(input_path)
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error splitting PDF: {e}")
        os.remove(input_path)
        raise HTTPException(status_code=500, detail=str(e))
