import fitz  # PyMuPDF
import subprocess
import pikepdf
import os
import logging
import uuid
from pathlib import Path
from tempfile import NamedTemporaryFile

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

QUALITY_TO_GS_SETTINGS = {
    "smart": "/ebook",
    "balanced": "/ebook",
    "high": "/prepress",
    "best": "/prepress",
    "medium": "/printer",
    "low": "/screen",
    "archive": "/default",
    "default": "/default",
    "screen": "/screen",
    "ebook": "/ebook",
    "printer": "/printer",
    "prepress": "/prepress",
}


def normalize_quality(quality: str) -> str:
    normalized = quality.strip().lower().lstrip("/")
    if normalized not in QUALITY_TO_GS_SETTINGS:
        allowed = ", ".join(sorted(QUALITY_TO_GS_SETTINGS.keys()))
        raise ValueError(f"Invalid quality preset '{quality}'. Allowed values: {allowed}")
    return QUALITY_TO_GS_SETTINGS[normalized]


def compress_pdf(input_path: str, quality: str = "smart"):
    gs_quality = normalize_quality(quality)
    logging.info(f"Starting PDF compression for: {input_path} with quality: {gs_quality}")

    input_path = Path(input_path)
    output_dir = input_path.parent

    output_path = output_dir / f"{uuid.uuid4().hex}.pdf"
    
    logging.info("Optimizing with PyMuPDF...")
    doc = fitz.open(input_path)

    with NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
        temp = temp_file.name

    doc.save(
        temp,
        garbage=4,      # remove unused objects
        deflate=True,   # compress streams
        clean=True      # clean up PDF structure
    )

    doc.close()
    logging.info(f"Saved temporary optimized file to: {temp}")

    logging.info("Compressing with Ghostscript...")
    command = [
        "gs",
        "-sDEVICE=pdfwrite",
        "-dCompatibilityLevel=1.4",
        f"-dPDFSETTINGS={gs_quality}",
        "-dNOPAUSE",
        "-dQUIET",
        "-dBATCH",
        f"-sOutputFile={output_path}",
        temp,
    ]

    subprocess.run(command, check=True)
    logging.info(f"Ghostscript compression successful. Output at: {output_path}")

    logging.info(f"Removing temporary file: {temp}")
    os.remove(temp)

    # Optimize with pikepdf
    logging.info("Optimizing with pikepdf...")
    with pikepdf.open(output_path, allow_overwriting_input=True) as pdf:
        pdf.save(output_path, linearize=True)
    logging.info("pikepdf optimization successful.")

    logging.info(f"PDF compression finished. Final file at: {output_path}")
    return output_path
