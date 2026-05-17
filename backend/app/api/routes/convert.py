from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from app.services.conversion.image_to_pdf import convert_images_to_pdf
from app.services.conversion.word_to_pdf_service import convert_word_to_pdf
from app.services.conversion.ppt_to_pdf import convert_ppt_to_pdf
import os
import tempfile
import logging
from typing import List

router = APIRouter()

@router.post("/convert/images-to-pdf/")
async def images_to_pdf_endpoint(files: List[UploadFile] = File(...)):
    """Endpoint to convert one or more images to a single PDF."""
    input_paths = []
    temp_files = []
    try:
        for file in files:
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.write(await file.read())
            input_paths.append(temp_file.name)
            temp_files.append(temp_file)

        output_dir = tempfile.gettempdir()
        output_path = convert_images_to_pdf(input_paths, output_dir)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            os.remove(file_path)
            for temp_file in temp_files:
                os.remove(temp_file.name)

        return StreamingResponse(
            file_iterator(output_path),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=converted.pdf"}
        )
    except Exception as e:
        logging.error(f"Error converting images to PDF: {e}")
        for temp_file in temp_files:
            os.remove(temp_file.name)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/convert/word-to-pdf/")
async def word_to_pdf_endpoint(file: UploadFile = File(...)):
    """Endpoint to convert a Word document to PDF."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".docx") as temp_input_file:
            temp_input_file.write(await file.read())
            input_path = temp_input_file.name

        output_dir = tempfile.gettempdir()
        output_path = convert_word_to_pdf(input_path, output_dir)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            os.remove(file_path)
            os.remove(input_path)

        return StreamingResponse(
            file_iterator(str(output_path)),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=converted.pdf"}
        )
    except Exception as e:
        logging.error(f"Error converting Word to PDF: {e}")
        os.remove(input_path)
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/convert/ppt-to-pdf/")
async def ppt_to_pdf_endpoint(file: UploadFile = File(...)):
    """Endpoint to convert a PowerPoint presentation to PDF."""
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as temp_input_file:
            temp_input_file.write(await file.read())
            input_path = temp_input_file.name

        output_dir = tempfile.gettempdir()
        output_path = convert_ppt_to_pdf(input_path, output_dir)

        def file_iterator(file_path):
            with open(file_path, "rb") as f:
                yield from f
            os.remove(file_path)
            os.remove(input_path)

        return StreamingResponse(
            file_iterator(str(output_path)),
            media_type="application/pdf",
            headers={"Content-Disposition": f"attachment; filename=converted.pdf"}
        )
    except Exception as e:
        logging.error(f"Error converting PowerPoint to PDF: {e}")
        os.remove(input_path)
        raise HTTPException(status_code=500, detail=str(e))
