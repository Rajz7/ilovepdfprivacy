from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.services.pdf.merge_service import merge_pdfs
import os
import tempfile
import logging
from typing import List

router = APIRouter()

@router.post("/merge-pdf/")
async def merge_pdf_endpoint(files: List[UploadFile] = File(...)):
    """Endpoint to merge multiple PDF files."""
    input_paths = []
    temp_files = []
    try:
        # Create temporary files to store the uploaded PDFs
        for file in files:
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
            temp_file.write(await file.read())
            input_paths.append(temp_file.name)
            temp_files.append(temp_file)

        # Define output path
        output_dir = tempfile.gettempdir()
        output_filename = "merged.pdf"
        output_path = os.path.join(output_dir, output_filename)

        # Merge the PDFs
        merge_pdfs(input_paths, output_dir, output_filename)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            # Clean up the files after sending the response
            os.remove(file_path)
            for temp_file in temp_files:
                os.remove(temp_file.name)

        return StreamingResponse(
            file_iterator(output_path),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={output_filename}"}
        )

    except Exception as e:
        logging.error(f"Error merging PDFs: {e}")
        # Clean up temp files in case of error
        for temp_file in temp_files:
            os.remove(temp_file.name)
        raise HTTPException(status_code=500, detail=str(e))
