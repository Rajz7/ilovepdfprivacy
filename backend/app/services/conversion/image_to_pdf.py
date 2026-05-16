import img2pdf
from PIL import Image
import os
import uuid

def convert_image_to_pdf(image_path):
    image = Image.open(image_path)
    pdf_path = image_path[:image_path.rfind('.')]
    pdf_path += os.path.join(f"{uuid.uuid4()}.pdf")

    pdf_bytes = img2pdf.convert(image.filename)

    file = open(pdf_path, "wb")

    file.write(pdf_bytes)

    image.close()

    file.close()

    print(f"Successfully made pdf file: {pdf_path}")
    return pdf_path