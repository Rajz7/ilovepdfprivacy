from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.services.pdf.compress_service import compress_pdf
import os
import tempfile
import logging

router = APIRouter()

@router.post("/compress-pdf/")
async def compress_pdf_endpoint(file: UploadFile = File(...), preset: str = "smart"):
    """Endpoint to compress a PDF file."""
    try:
        # Create a temporary file to store the uploaded PDF
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_input_file:
            temp_input_file.write(await file.read())
            input_path = temp_input_file.name

        output_path = compress_pdf(input_path, preset)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            # Clean up the files after sending the response
            os.remove(file_path)
            os.remove(input_path)   

        return StreamingResponse(
            file_iterator(output_path),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename={os.path.basename(output_path)}"}
        )

    except ValueError as e:
        logging.error(f"Invalid compression preset: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Error compressing PDF: {e}")
        raise HTTPException(status_code=500, detail=str(e))

    