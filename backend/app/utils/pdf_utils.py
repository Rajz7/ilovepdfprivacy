import os
from reportlab.pdfgen import canvas

def create_pdf_file(file_path: str, file_name: str):
    full_path = os.path.join(file_path, file_name)

    pdf = canvas.Canvas(full_path)
    pdf.save()

    return full_path


    