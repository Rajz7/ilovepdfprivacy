from PyPDF2 import PdfWriter
from app.utils.pdf_utils import create_pdf_file

def merge_pdfs(input_pdfs: list, output_path: str, output_file_name: str):
    if not output_file_name.strip().lower().endswith(".pdf"):
        output_file_name += ".pdf"

    output_path = create_pdf_file(output_path, output_file_name)

    pdf_writer = PdfWriter()
    for pdf in input_pdfs:
        pdf_writer.append(pdf)
    
    with open(output_path, 'wb') as output_path:
        pdf_writer.write(output_path)


