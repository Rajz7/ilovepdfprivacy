import fitz  # PyMuPDF
import subprocess
import pikepdf
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compress_pdf(input_path: str, quality: str = "/ebook"):
    logging.info(f"Starting PDF compression for: {input_path} with quality: {quality}")
    temp = "temp_compressed.pdf"
    output_path = input_path.replace(".pdf", "_compressed.pdf")
    files = os.listdir(os.path.dirname(input_path))

    if os.path.basename(output_path) in files:
        i = 1
        while os.path.basename(output_path) in files:
            output_path = input_path.replace(".pdf", f"_compressed_{i}.pdf")
            i += 1
    
    logging.info("Optimizing with PyMuPDF...")
    doc = fitz.open(input_path)

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
        f"-dPDFSETTINGS={quality}",
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

input_path = "/home/lamborghini/Downloads/test.pdf"
compress_pdf(input_path)
